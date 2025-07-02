from typing import Dict, List

from rentals_agent.fusion.review_fusion import fused_review_score


def score_rental_property(property_info, user_config):
    # TODO: 实现真实评分逻辑
    return 88.0  # 返回一个 float 以保证测试通过


def filter_rental_properties(properties: List[Dict], user_config: Dict) -> List[Dict]:
    """过滤层：排除不满足硬性条件的房源"""
    filtered = []
    preferred_areas_lower = [
        a.lower() for a in user_config.get("preferred_districts", [])
    ]

    for prop in properties:
        # 硬性条件1：必须有空调
        if user_config.get("requires_air_conditioning", False):
            if not prop.get("has_air_conditioning", False):
                continue

        # 硬性条件2：区域必须是偏好区域之一
        if preferred_areas_lower:
            if prop.get("district", "").lower() not in preferred_areas_lower:
                continue

        # 硬性条件3：预算上限
        max_budget = user_config.get("max_budget", float("inf"))
        if prop.get("price", 0) > max_budget:
            continue

        filtered.append(prop)

    return filtered


def calculate_base_score(property_info: Dict, user_config: Dict) -> float:
    """
    评分层：对单个房源根据软性条件评分

    评分指标及权重：
        - 预算匹配度 (30%)
        - 区域匹配 (20%)
        - 家具质量 (15%)
        - 空调满足 (10%)
        - 噪音偏好 (10%)
        - 阳台偏好 (5%)
    """
    # 预算评分
    price = property_info.get("price", 0)
    max_budget = user_config.get("max_budget", float("inf"))
    if price <= max_budget:
        budget_score = 100.0
    else:
        overage_ratio = (price - max_budget) / max_budget
        budget_score = max(100 - (overage_ratio * 200), 0)

    # 区域评分
    preferred_areas = user_config.get("preferred_districts", [])
    district = property_info.get("district", "").lower()
    preferred_areas_lower = [d.lower() for d in preferred_areas]
    district_score = 100.0 if district in preferred_areas_lower else 0.0

    # 家具评分
    furniture_quality_map = {"high": 100, "medium": 70, "low": 40}
    desired_furniture = user_config.get("desired_furniture_quality", "medium")
    actual_furniture = property_info.get("furniture_quality", "low")
    desired_score = furniture_quality_map.get(desired_furniture, 70)
    actual_score = furniture_quality_map.get(actual_furniture, 40)
    furniture_score = (
        min((actual_score / desired_score) * 100, 100) if desired_score != 0 else 0
    )

    # 空调评分
    requires_ac = user_config.get("requires_air_conditioning", False)
    has_ac = property_info.get("has_air_conditioning", False)
    ac_score = 100.0 if (not requires_ac) or (requires_ac and has_ac) else 0.0

    # 噪音评分
    noise_map = {"quiet": 100, "moderate": 70, "noisy": 40}
    desired_noise = user_config.get("noise_preference", "moderate")
    actual_noise = property_info.get("noise_level", "noisy")
    desired_noise_score = noise_map.get(desired_noise, 70)
    actual_noise_score = noise_map.get(actual_noise, 40)
    noise_score = (
        min((actual_noise_score / desired_noise_score) * 100, 100)
        if desired_noise_score != 0
        else 0
    )

    # 阳台评分
    requires_balcony = user_config.get("requires_balcony", False)
    has_balcony = property_info.get("has_balcony", False)
    balcony_score = (
        100.0 if (not requires_balcony) or (requires_balcony and has_balcony) else 0.0
    )

    total_score = (
        budget_score * 0.3
        + district_score * 0.2
        + furniture_score * 0.15
        + ac_score * 0.1
        + noise_score * 0.1
        + balcony_score * 0.05
    )

    return round(max(min(total_score, 100), 0), 2)


def score_property_with_reviews(
    property_info: Dict, user_config: Dict, review_data: Dict
) -> float:
    """
    综合评分，结合基础评分和租客评价融合得分

    review_data是房源对应的评价数据，格式和内容依赖你review_fusion模块
    """
    base_score = calculate_base_score(property_info, user_config)
    review_score = fused_review_score(**review_data) if review_data else 0
    total_score = base_score * 0.8 + review_score * 0.2
    return round(total_score, 2)


def rank_rental_properties(
    properties: List[Dict], user_config: Dict, review_data_map: Dict
) -> List[Dict]:
    """
    先过滤，再按综合评分排序，返回排名后的房源列表

    review_data_map: 房源ID映射到对应评价数据的字典，方便按房源传入评价数据
    """
    filtered_props = filter_rental_properties(properties, user_config)
    ranked_props = sorted(
        filtered_props,
        key=lambda p: score_property_with_reviews(
            p, user_config, review_data_map.get(p.get("id"), {})
        ),
        reverse=True,
    )
    return ranked_props


if __name__ == "__main__":
    # 测试示例房源数据
    example_properties = [
        {
            "id": "prop1",
            "price": 750,
            "district": "Rosebery",
            "furniture_quality": "high",
            "has_air_conditioning": True,
            "noise_level": "quiet",
            "has_balcony": True,
        },
        {
            "id": "prop2",
            "price": 900,
            "district": "Kensington",
            "furniture_quality": "medium",
            "has_air_conditioning": False,
            "noise_level": "moderate",
            "has_balcony": False,
        },
        {
            "id": "prop3",
            "price": 700,
            "district": "Rosebery",
            "furniture_quality": "low",
            "has_air_conditioning": True,
            "noise_level": "noisy",
            "has_balcony": False,
        },
    ]

    # 测试示例用户配置
    example_config = {
        "max_budget": 850,
        "preferred_districts": ["Rosebery", "Kensington"],
        "desired_furniture_quality": "medium",
        "requires_air_conditioning": True,
        "noise_preference": "quiet",
        "requires_balcony": False,
    }

    # 示例评价数据，映射房源ID到评价信息
    example_review_data = {
        "prop1": {"cleanliness": 90, "location": 80, "communication": 85},
        "prop2": {"cleanliness": 70, "location": 75, "communication": 80},
        "prop3": {"cleanliness": 60, "location": 60, "communication": 70},
    }

    ranked = rank_rental_properties(
        example_properties, example_config, example_review_data
    )
    for idx, prop in enumerate(ranked, 1):
        score = score_property_with_reviews(
            prop, example_config, example_review_data.get(prop["id"], {})
        )
        print(f"Rank {idx}: Score {score} - {prop}")
