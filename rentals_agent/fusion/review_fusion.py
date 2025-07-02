from typing import Optional


def fused_review_score(
    cleanliness: Optional[float] = None,
    location: Optional[float] = None,
    communication: Optional[float] = None,
    overall: Optional[float] = None,
) -> float:
    """
    评价融合函数，计算综合评分。
    只考虑传入的有效参数，缺失的字段不计权重，权重自动归一化。

    权重示例（可调整）：
      cleanliness: 0.3
      location: 0.3
      communication: 0.3
      overall: 0.1

    如果传入的字段为空或None，则自动忽略对应权重。
    """
    weights = {
        "cleanliness": 0.3,
        "location": 0.3,
        "communication": 0.3,
        "overall": 0.1,
    }

    scores = {
        "cleanliness": cleanliness,
        "location": location,
        "communication": communication,
        "overall": overall,
    }

    # 过滤掉None的项
    valid_scores = {k: v for k, v in scores.items() if v is not None}

    if not valid_scores:
        return 0.0  # 没有有效评分时，返回0分

    # 归一化权重
    total_weight = sum(weights[k] for k in valid_scores.keys())
    normalized_weights = {k: weights[k] / total_weight for k in valid_scores.keys()}

    # 计算加权平均分
    fused_score = sum(
        valid_scores[k] * normalized_weights[k] for k in valid_scores.keys()
    )

    return round(fused_score, 2)
