import random
from flask import Flask, jsonify

app = Flask(__name__)

# القائمة التي تحتوي على الكلمات
research = [
    "猫", "狗", "鸟", "鱼", "兔子", "龙", "熊猫", "象", "蝴蝶", "草原", "山", "河", 
    "海洋", "星星", "月亮", "太阳", "花", "树", "草", "蓝天", "白云", "风", "雨", 
    "雪", "电脑", "手机", "汽车", "自行车", "服装", "鞋子", "帽子", "手提包", 
    "爱", "心", "亲吻", "婚姻", "家庭", "朋友", "笑容", "幸福", "成功", "学业", 
    "工作", "旅行", "音乐", "电影", "艺术", "文学", "食物", "饮料", "美食", 
    "健康", "运动", "假期", "梦想", "冒险", "教育", "科学", "技术", "创新", 
    "环境", "保护", "慈善", "志愿者", "和平", "友谊", "团结", "信任", "合作", 
    "领导", "政府", "政治", "法律", "社会", "经济", "移民", "文化", "宗教", 
    "节日", "传统", "现代", "国际", "语言", "文字", "阅读", "写作", "绘画", 
    "音乐会", "舞蹈", "戏剧", "时尚", "设计", "制造业", "电子商务", "金融", 
    "投资", "股市", "创业", "环保", "可持续发展", "新能源", "城市规划", 
    "交通", "高速铁路", "航空", "海运", "人工智能", "机器人", "太空探索", 
    "星际旅行", "基因工程", "生命科学", "医疗", "疫苗", "大学", "学科", 
    "研究", "科学家", "教授", "学生", "语言学", "历史学", "数学", "物理学", 
    "化学", "生物学", "外交", "国际关系", "军事", "警察", "司法", "人权", 
    "民主", "社交媒体", "电视", "广播", "报纸", "网络", "游戏", "艺术品", 
    "收藏", "摄影", "漫画", "喜剧", "悲剧", "爱情片", "恐怖片", "科幻片", 
    "动作片", "纪录片", "时装", "运动服", "风衣", "旗袍", "西装", "礼服", 
    "休闲装", "时尚设计师", "时装表演", "时尚杂志", "高跟鞋", "运动鞋", 
    "皮包", "钱包", "珠宝", "手表", "太阳镜", "戒指", "领带", "围巾", "手套", 
    "毛衣", "丝绸", "棉布", "皮革", "毛皮", "高尔夫球", "足球", "篮球", "游泳", 
    "登山", "滑雪", "自行车赛", "赛车", "马术", "瑜伽", "武术", "舞蹈比赛", 
    "艺术节", "体育比赛", "冠军", "勇气", "希望", "忍耐", "快乐", "幽默", 
    "美丽", "勤奋", "耐心", "尊重"
]

@app.route('/')
def get_random_word():
    word = random.choice(research)
    return jsonify({"word": word})

if __name__ == '__main__':
    app.run(debug=True)
