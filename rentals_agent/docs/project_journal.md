📘 rentals_agent Project Journal

持续记录项目开发的心路历程、遇到的问题、思考与调整，便于未来回顾与复用在其他实用型项目。

⸻

🪐 Project Purpose Recap
	1.	练习 Python 和项目开发（requests / pandas / playwright / 可视化 / 项目结构化管理），形成能独立做 vibe coding 的能力。
	2.	真正帮助 9 月入住悉尼租房，提前监控价格区间、找到合适可租房源。

⸻

🚩 2025-07-01

✅ 动作
	•	开始使用 Trae + PyCharm 开发 rentals_agent 项目。
	•	搭建 requests 抓取 domain.com.au 与 realestate.com.au 接口测试。

🌀 遇到问题
	•	抓取时遇到 Cloudflare 验证、403 报错，无法直接通过 API 获取完整房源数据。
	•	realestate.com.au 动态加载复杂，难以通过简单 requests 获取。

💡 思考
	•	若继续强攻反爬，效率低且不稳定。
	•	项目目的不仅是技术练习，还要确保真实租房需求落地。

⸻

🚩 2025-07-02

✅ 动作
	•	分析网站前端结构，尝试使用 selenium 模拟加载获取房源列表。
	•	学习 Playwright 的可行性，计划替代 selenium 提高稳定性和速度。
	•	梳理抓取数据字段（标题、价格、地址、卧室、链接）。

💡 思考
	•	确定只抓取 目标 suburb（Kingsford, Kensington, Randwick, Waterloo, Zetland, Rosebery） 的前 5-10 条房源。
	•	半自动 + 手动录入结合，提高实用效率。
	•	开始考虑 Airtable / Notion 管理房源信息。

⸻

🚩 2025-07-03

✅ 动作
	•	继续尝试 domain.com.au 的 API 抓取优化，验证抓取参数无效。
	•	明确当前技术瓶颈并决定不再花费过多时间攻坚反爬。
	•	开始准备构建项目计划的每日节奏。

💡 思考
	•	项目应帮助实际租房，不应陷入技术 Debug 漩涡。
	•	可作为练习项目保留小规模抓取与可视化逻辑。
	•	租房实用部分转向使用 Facebook Marketplace、微信群同步找房，半自动录入数据库管理。

⸻

🚩 2025-07-04（今日）

✅ 动作
	•	确定 B+D 路线（半自动 + 租房整体流程优化）。
	•	确认 Playwright 技术栈可行，准备编写首个抓取 demo。
	•	准备在项目内创建 docs/project_journal.md 并记录项目思路和节奏。

💡 思考
	•	项目目标进一步明确：抓取价格范围和部分房源用于可视化和辅助决策，真正实用找房依赖多渠道半自动组合。
	•	未来可将项目技术迁移至机票比价 / 超市比价 / 留学申请监控等场景。

⸻

✅ 下一步计划
	•	创建 Airtable / Notion 租房数据库表结构，便于管理潜在房源。
	•	编写 Playwright 抓取悉尼指定 suburb 前 5 条房源 demo，测试完整流程。
	•	输出初版价格分布可视化柱状图（suburb vs 平均价格）。
	•	建立每周抓取 - 更新数据库 - 看房 - 决策的完整租房节奏。
	•	写完后 push 到 GitHub，形成可公开展示的项目履历。

⸻

本 journal 文件将持续更新，记录每天的开发与思路演变，帮助持续聚焦在【完成完整闭环】与【真正帮助租房】的双目标上，同时便于未来迁移方法论到其他 vibe coding 项目中。