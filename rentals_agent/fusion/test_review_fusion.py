import unittest

from rentals_agent.fusion.review_fusion import fused_review_score


class TestFusedReviewScore(unittest.TestCase):

    def test_all_fields_provided(self):
        score = fused_review_score(
            cleanliness=90, location=80, communication=85, overall=70
        )
        # 计算加权平均，预期大致为：
        # (90*0.3 + 80*0.3 + 85*0.3 + 70*0.1) = 27 + 24 + 25.5 + 7 = 83.5
        self.assertAlmostEqual(score, 83.5, places=1)

    def test_missing_overall(self):
        score = fused_review_score(cleanliness=90, location=80, communication=85)
        # 权重重新归一化后：
        # 每个权重 = 0.3 / (0.3*3) = 1/3 ≈ 0.3333
        # 计算：(90 + 80 + 85) / 3 = 85.0
        self.assertAlmostEqual(score, 85.0, places=1)

    def test_only_one_field(self):
        score = fused_review_score(cleanliness=70)
        # 只有一个字段，权重自动归一，返回70
        self.assertEqual(score, 70)

    def test_no_fields(self):
        score = fused_review_score()
        # 没有输入评分，返回0
        self.assertEqual(score, 0)

    def test_some_fields_none(self):
        score = fused_review_score(cleanliness=80, location=None, communication=90)
        # 归一化权重为0.3和0.3，共0.6
        # 新权重分别为0.3/0.6=0.5
        # 计算：80*0.5 + 90*0.5 = 85.0
        self.assertAlmostEqual(score, 85.0, places=1)


if __name__ == "__main__":
    unittest.main()
