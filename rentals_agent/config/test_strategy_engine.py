import os
import sys
import unittest

from rentals_agent.config.strategy_engine import (filter_rental_properties,
                                                  rank_rental_properties,
                                                  score_rental_property)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


class TestStrategyEngine(unittest.TestCase):

    def setUp(self):
        self.user_config = {
            "max_budget": 850,
            "preferred_districts": ["Rosebery", "Kensington"],
            "desired_furniture_quality": "medium",
            "requires_air_conditioning": True,
            "noise_preference": "quiet",
            "requires_balcony": False,
        }

        self.properties = [
            {
                "price": 750,
                "district": "Rosebery",
                "furniture_quality": "high",
                "has_air_conditioning": True,
                "noise_level": "quiet",
                "has_balcony": True,
            },
            {
                "price": 900,
                "district": "Kensington",
                "furniture_quality": "medium",
                "has_air_conditioning": False,
                "noise_level": "moderate",
                "has_balcony": False,
            },
            {
                "price": 700,
                "district": "Rosebery",
                "furniture_quality": "low",
                "has_air_conditioning": True,
                "noise_level": "noisy",
                "has_balcony": False,
            },
        ]

    def test_filter_rental_properties(self):
        filtered = filter_rental_properties(self.properties, self.user_config)
        # 第二个房源没有空调，应该被过滤掉
        self.assertEqual(len(filtered), 2)
        for prop in filtered:
            self.assertTrue(prop["has_air_conditioning"])

    def filter_rental_properties(properties, user_config):
        filtered = []
        for prop in properties:
            # 其他过滤条件...

            # 一人居住需求
            if user_config.get("single_occupancy_required", False):
                # 假设房源字段里有 'max_occupants' 或 'room_type' 来判断
                if "max_occupants" in prop and prop["max_occupants"] > 1:
                    continue
                if "room_type" in prop and prop["room_type"] != "single":
                    continue

            filtered.append(prop)
        return filtered

    def test_score_rental_property(self):
        prop = self.properties[0]
        score = score_rental_property(prop, self.user_config)
        self.assertIsInstance(score, float)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)

    def test_rank_rental_properties(self):
        ranked = rank_rental_properties(
            self.properties, self.user_config, self.review_data_map
        )  # 过滤层排除一个，剩下两个，排序后返回
        self.assertEqual(len(ranked), 2)
        # 最高分房源排在第一个
        first_score = score_rental_property(ranked[0], self.user_config)
        second_score = score_rental_property(ranked[1], self.user_config)
        self.assertGreaterEqual(first_score, second_score)


if __name__ == "__main__":
    unittest.main()
