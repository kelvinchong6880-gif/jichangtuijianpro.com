// 各机场套餐结构化数据（来源：各机场官网套餐页，2026-10-04 核对）。
// 改价格 / 流量 / 优惠码只需要改这里；首页、性价比、便宜、对比、排行榜页会自动重新计算。
// billing: Monthly 月付 | Quarterly 季付 | Yearly 年付 | One-Time 一次性不限时
// traffic: 周期套餐为“每月流量 GB”，一次性套餐为“总流量 GB”；custom: 定制/独享线路，不参与价格排序
export type Billing = 'Monthly' | 'Quarterly' | 'Yearly' | 'One-Time';
export interface PlanItem { name: string; price: number; billing: Billing; traffic: number | null; custom?: boolean }
export interface BrandPlans {
  file: string; lines: string[]; streaming: boolean | null; ai: boolean | null;
  promo: string | null; nodeRegions: string | null; plans: PlanItem[];
}
export const PLANS: Record<string, BrandPlans> = {
  "sogo": {
    "file": "sogo",
    "lines": [
      "IPLC",
      "IEPL"
    ],
    "streaming": true,
    "ai": true,
    "promo": "sogo10000",
    "nodeRegions": "香港×20、台湾×5、日本×10、新加坡×10、美国×10、马来西亚×2、英国、法国、德国、土耳其、泰国、巴西等",
    "plans": [
      {
        "name": "小包-年付版",
        "price": 98,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "基础版",
        "price": 25,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "优选版",
        "price": 45,
        "billing": "Monthly",
        "traffic": 350
      },
      {
        "name": "强化版",
        "price": 80,
        "billing": "Monthly",
        "traffic": 550
      },
      {
        "name": "顶配版",
        "price": 150,
        "billing": "Monthly",
        "traffic": 1050
      },
      {
        "name": "SOGO基础餐不限时版",
        "price": 120,
        "billing": "One-Time",
        "traffic": 120
      },
      {
        "name": "SOGO优选餐不限时版",
        "price": 250,
        "billing": "One-Time",
        "traffic": 250
      },
      {
        "name": "SOGO强化餐不限时版",
        "price": 450,
        "billing": "One-Time",
        "traffic": 500
      },
      {
        "name": "SOGO至尊餐不限时版",
        "price": 850,
        "billing": "One-Time",
        "traffic": 1000
      }
    ]
  },
  "feimao": {
    "file": "飞猫",
    "lines": [
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": "flycat888",
    "nodeRegions": "香港 x20、台湾 x10、日本 x10、新加坡 x10、美国 x10、韩国 x3、马来西亚、越南、菲律宾、泰国、印度、英国、法国、德国、阿根廷等",
    "plans": [
      {
        "name": "飞猫 · 学生版",
        "price": 84,
        "billing": "Yearly",
        "traffic": 50
      },
      {
        "name": "飞猫 · 星耀版",
        "price": 25,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "飞猫 · 星环版",
        "price": 45,
        "billing": "Monthly",
        "traffic": 300
      },
      {
        "name": "飞猫 · 银河版",
        "price": 85,
        "billing": "Monthly",
        "traffic": 600
      },
      {
        "name": "飞猫 · 宇宙版",
        "price": 150,
        "billing": "Monthly",
        "traffic": 1000
      },
      {
        "name": "飞猫 · 不限时套餐",
        "price": 680,
        "billing": "One-Time",
        "traffic": 1000
      },
      {
        "name": "飞猫 · 定制套餐",
        "price": 550,
        "billing": "Monthly",
        "traffic": 500,
        "custom": true
      }
    ]
  },
  "weifeng": {
    "file": "微风",
    "lines": [
      "IPLC"
    ],
    "streaming": null,
    "ai": null,
    "promo": "weifeng90",
    "nodeRegions": "香港、台湾、美国、新加坡、马来西亚、日本等",
    "plans": [
      {
        "name": "清风",
        "price": 137,
        "billing": "Yearly",
        "traffic": 100
      },
      {
        "name": "乘风",
        "price": 27,
        "billing": "Monthly",
        "traffic": 200
      },
      {
        "name": "破风",
        "price": 57,
        "billing": "Monthly",
        "traffic": 500
      },
      {
        "name": "御风",
        "price": 127,
        "billing": "Monthly",
        "traffic": 1200
      },
      {
        "name": "信风 ·不限时",
        "price": 200,
        "billing": "One-Time",
        "traffic": 270
      },
      {
        "name": "长风·不限时",
        "price": 370,
        "billing": "One-Time",
        "traffic": 570
      }
    ]
  },
  "yuzhou": {
    "file": "宇宙",
    "lines": [
      "IPLC",
      "IEPL"
    ],
    "streaming": true,
    "ai": true,
    "promo": "YUZHOU553",
    "nodeRegions": "香港×20、台湾×5、日本×10、新加坡×10、美国×10、马来西亚、德国等",
    "plans": [
      {
        "name": "星云年付小包",
        "price": 96,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "行星基础版",
        "price": 25,
        "billing": "Monthly",
        "traffic": 160
      },
      {
        "name": "恒星标准版",
        "price": 50,
        "billing": "Monthly",
        "traffic": 300
      },
      {
        "name": "星系专业版",
        "price": 100,
        "billing": "Monthly",
        "traffic": 700
      },
      {
        "name": "寰宇旗舰版",
        "price": 200,
        "billing": "Monthly",
        "traffic": 1500
      },
      {
        "name": "行星基础版（不限时）",
        "price": 110,
        "billing": "One-Time",
        "traffic": 120
      },
      {
        "name": "恒星标准版（不限时）",
        "price": 220,
        "billing": "One-Time",
        "traffic": 200
      }
    ]
  },
  "firefly": {
    "file": "firefly",
    "lines": [
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": "firefly",
    "nodeRegions": "香港、台湾、美国、新加坡、马来西亚、日本等",
    "plans": [
      {
        "name": "Firefly年付版",
        "price": 96,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "Firefly Lite",
        "price": 25,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "Firefly Plus",
        "price": 45,
        "billing": "Monthly",
        "traffic": 300
      },
      {
        "name": "Firefly Blaze",
        "price": 85,
        "billing": "Monthly",
        "traffic": 600
      },
      {
        "name": "Firefly Nova",
        "price": 150,
        "billing": "Monthly",
        "traffic": 1000
      },
      {
        "name": "Firefly不限时",
        "price": 100,
        "billing": "One-Time",
        "traffic": 100
      }
    ]
  },
  "wuyou": {
    "file": "无忧",
    "lines": [
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": "wuyou",
    "nodeRegions": "香港、台湾、美国、新加坡、马来西亚、日本等",
    "plans": [
      {
        "name": "MINI链接",
        "price": 79,
        "billing": "Yearly",
        "traffic": 40
      },
      {
        "name": "舒心链接",
        "price": 19,
        "billing": "Monthly",
        "traffic": 100
      },
      {
        "name": "省心链接",
        "price": 33,
        "billing": "Monthly",
        "traffic": 200
      },
      {
        "name": "随心链接",
        "price": 77,
        "billing": "Monthly",
        "traffic": 500
      },
      {
        "name": "忘忧链接",
        "price": 117,
        "billing": "Monthly",
        "traffic": 1000
      },
      {
        "name": "100G永久不限时 无忧链接",
        "price": 108,
        "billing": "One-Time",
        "traffic": 100
      },
      {
        "name": "300G永久不限时 无忧链接",
        "price": 298,
        "billing": "One-Time",
        "traffic": 300
      }
    ]
  },
  "kuajie": {
    "file": "跨界",
    "lines": [
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": "kuajie",
    "nodeRegions": "香港、台湾、美国、新加坡、马来西亚、日本等",
    "plans": [
      {
        "name": "跨界年付版",
        "price": 96,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "轻云 Lite",
        "price": 20,
        "billing": "Monthly",
        "traffic": 120
      },
      {
        "name": "跃云 Leap",
        "price": 40,
        "billing": "Monthly",
        "traffic": 330
      },
      {
        "name": "凌云 Soar",
        "price": 90,
        "billing": "Monthly",
        "traffic": 830
      },
      {
        "name": "无界 Infinity",
        "price": 130,
        "billing": "Monthly",
        "traffic": 1800
      }
    ]
  },
  "shanyue": {
    "file": "闪跃",
    "lines": [
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": "shanyue",
    "nodeRegions": "香港、台湾、美国、新加坡、马来西亚、日本等",
    "plans": [
      {
        "name": "闪跃年付版",
        "price": 96,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "闪动 (Flicker)",
        "price": 24,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "飞跃 (Leap)",
        "price": 44,
        "billing": "Monthly",
        "traffic": 300
      },
      {
        "name": "瞬移 (Teleport)",
        "price": 84,
        "billing": "Monthly",
        "traffic": 600
      },
      {
        "name": "跃迁 (Warp)",
        "price": 134,
        "billing": "Monthly",
        "traffic": 1000
      }
    ]
  },
  "lingmao": {
    "file": "灵猫",
    "lines": [
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": "lingmao",
    "nodeRegions": "香港、台湾、美国、新加坡、马来西亚、日本等",
    "plans": [
      {
        "name": "灵猫·年付小包",
        "price": 85,
        "billing": "Yearly",
        "traffic": 45
      },
      {
        "name": "灵猫·年付Small",
        "price": 195,
        "billing": "Yearly",
        "traffic": 150
      },
      {
        "name": "灵猫·年付Big",
        "price": 295,
        "billing": "Yearly",
        "traffic": 300
      },
      {
        "name": "灵猫·季付Big",
        "price": 125,
        "billing": "Quarterly",
        "traffic": 300
      },
      {
        "name": "灵猫·月付Small",
        "price": 25,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "灵猫·月付Big",
        "price": 45,
        "billing": "Monthly",
        "traffic": 300
      }
    ]
  },
  "edgenova": {
    "file": "edgenova",
    "lines": [
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": null,
    "nodeRegions": null,
    "plans": [
      {
        "name": "EdgeNova 入门月付",
        "price": 15,
        "billing": "Monthly",
        "traffic": 50
      },
      {
        "name": "EdgeNova 45GB 年付",
        "price": 108,
        "billing": "Yearly",
        "traffic": 45
      },
      {
        "name": "EdgeNova 120GB 月付",
        "price": 25,
        "billing": "Monthly",
        "traffic": 120
      },
      {
        "name": "EdgeNova 250GB 月付",
        "price": 50,
        "billing": "Monthly",
        "traffic": 250
      },
      {
        "name": "EdgeNova 499GB 月付",
        "price": 100,
        "billing": "Monthly",
        "traffic": 499
      },
      {
        "name": "EdgeNova 1TB 月付",
        "price": 200,
        "billing": "Monthly",
        "traffic": 1024
      }
    ]
  },
  "u1s1": {
    "file": "u1s1",
    "lines": [
      "IEPL"
    ],
    "streaming": true,
    "ai": true,
    "promo": "U1S1-80",
    "nodeRegions": null,
    "plans": [
      {
        "name": "u1s1 · 就是好用包",
        "price": 96,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "u1s1 · 普通人真够了包",
        "price": 20,
        "billing": "Monthly",
        "traffic": 120
      },
      {
        "name": "u1s1 · 你以为用不到包",
        "price": 40,
        "billing": "Monthly",
        "traffic": 300
      },
      {
        "name": "u1s1 · 瘾大就拉满包",
        "price": 100,
        "billing": "Monthly",
        "traffic": 700
      },
      {
        "name": "u1s1 · 我全都要包",
        "price": 180,
        "billing": "Monthly",
        "traffic": 1500
      },
      {
        "name": "u1s1 · 定制包",
        "price": 600,
        "billing": "Monthly",
        "traffic": null,
        "custom": true
      }
    ]
  },
  "yifan": {
    "file": "一翻",
    "lines": [
      "IEPL"
    ],
    "streaming": true,
    "ai": true,
    "promo": "1FLYYUN",
    "nodeRegions": "港/台/新/日/美等（60+ 专线节点）",
    "plans": [
      {
        "name": "轻享版",
        "price": 20,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "舒享版",
        "price": 35,
        "billing": "Monthly",
        "traffic": 350
      },
      {
        "name": "尊享版",
        "price": 55,
        "billing": "Monthly",
        "traffic": 600
      },
      {
        "name": "极致版",
        "price": 95,
        "billing": "Monthly",
        "traffic": 1200
      },
      {
        "name": "98¥ · 年付小包",
        "price": 98,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "轻享版 · 不限时包",
        "price": 100,
        "billing": "One-Time",
        "traffic": 100
      },
      {
        "name": "舒享版 · 不限时包",
        "price": 200,
        "billing": "One-Time",
        "traffic": 250
      },
      {
        "name": "尊享版 · 不限时包",
        "price": 400,
        "billing": "One-Time",
        "traffic": 500
      }
    ]
  },
  "ermao": {
    "file": "二猫",
    "lines": [
      "IEPL"
    ],
    "streaming": true,
    "ai": true,
    "promo": "ermao888",
    "nodeRegions": "港/台/新/日/美/德等地区（60+ 节点）",
    "plans": [
      {
        "name": "二猫云 · 100G不限时",
        "price": 99,
        "billing": "One-Time",
        "traffic": 100
      },
      {
        "name": "二猫年付小包",
        "price": 89,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "二猫云 · 白猫套餐",
        "price": 20,
        "billing": "Monthly",
        "traffic": 130
      },
      {
        "name": "二猫云 · 黑猫重度用户版",
        "price": 160,
        "billing": "Monthly",
        "traffic": 850
      },
      {
        "name": "二猫云 · 橘猫畅玩版",
        "price": 40,
        "billing": "Monthly",
        "traffic": 230
      },
      {
        "name": "二猫云 · 牛奶猫尊享版",
        "price": 80,
        "billing": "Monthly",
        "traffic": 430
      }
    ]
  },
  "guangnianti": {
    "file": "光年梯",
    "lines": [
      "IPLC",
      "IEPL"
    ],
    "streaming": true,
    "ai": true,
    "promo": null,
    "nodeRegions": null,
    "plans": [
      {
        "name": "年付限时套餐",
        "price": 89,
        "billing": "Yearly",
        "traffic": 50
      },
      {
        "name": "光年梯 入门版",
        "price": 18,
        "billing": "Monthly",
        "traffic": 110
      },
      {
        "name": "光年梯 晋级版",
        "price": 34,
        "billing": "Monthly",
        "traffic": 220
      },
      {
        "name": "光年梯 专业版",
        "price": 68,
        "billing": "Monthly",
        "traffic": 450
      },
      {
        "name": "光年梯 至尊版",
        "price": 130,
        "billing": "Monthly",
        "traffic": 900
      },
      {
        "name": "独享私人专线节点",
        "price": 680,
        "billing": "Monthly",
        "traffic": 500,
        "custom": true
      }
    ]
  },
  "guangsu": {
    "file": "光速",
    "lines": [
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": "AMM",
    "nodeRegions": "港、台、日、新、马、美、德、法、英、土、越等",
    "plans": [
      {
        "name": "光速云 · 轻量版",
        "price": 99,
        "billing": "Yearly",
        "traffic": 59
      },
      {
        "name": "光速云 · 极速版",
        "price": 23,
        "billing": "Monthly",
        "traffic": 138
      },
      {
        "name": "光速云 · 流光版",
        "price": 34,
        "billing": "Monthly",
        "traffic": 238
      },
      {
        "name": "光速云 · 量子版",
        "price": 68,
        "billing": "Monthly",
        "traffic": 450
      },
      {
        "name": "光速云 · 无界版",
        "price": 130,
        "billing": "Monthly",
        "traffic": 900
      },
      {
        "name": "光速云 · 不限时套餐",
        "price": 680,
        "billing": "One-Time",
        "traffic": 1000
      },
      {
        "name": "光速云 · 定制套餐",
        "price": 680,
        "billing": "Monthly",
        "traffic": 500,
        "custom": true
      }
    ]
  },
  "kexinyun": {
    "file": "可信云",
    "lines": [
      "IEPL"
    ],
    "streaming": true,
    "ai": true,
    "promo": "kxy80",
    "nodeRegions": "港/台/新/日/美等（60+ 专线节点）",
    "plans": [
      {
        "name": "可信云年付小包",
        "price": 96,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "可信云月付小包",
        "price": 15,
        "billing": "Monthly",
        "traffic": 60
      },
      {
        "name": "基础版（Basic）",
        "price": 25,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "标准版（Standard）",
        "price": 50,
        "billing": "Monthly",
        "traffic": 300
      },
      {
        "name": "专业版（Pro）",
        "price": 100,
        "billing": "Monthly",
        "traffic": 600
      },
      {
        "name": "旗舰版（Ultimate）",
        "price": 200,
        "billing": "Monthly",
        "traffic": 1200
      },
      {
        "name": "可信云轻量不限时",
        "price": 50,
        "billing": "One-Time",
        "traffic": 50
      }
    ]
  },
  "weitu": {
    "file": "唯兔",
    "lines": [
      "IEPL",
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": "rabbit",
    "nodeRegions": null,
    "plans": [
      {
        "name": "唯兔云 · 年付加强专线",
        "price": 120,
        "billing": "Yearly",
        "traffic": 75
      },
      {
        "name": "唯兔云 · 年付版限量款",
        "price": 79.9,
        "billing": "Yearly",
        "traffic": 45
      },
      {
        "name": "唯兔云 · 普通版",
        "price": 19.9,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "唯兔云 · 进阶版",
        "price": 29.9,
        "billing": "Monthly",
        "traffic": 200
      },
      {
        "name": "唯兔云 · 专业版",
        "price": 59.9,
        "billing": "Monthly",
        "traffic": 500
      },
      {
        "name": "唯兔云 · 至尊版",
        "price": 119.9,
        "billing": "Monthly",
        "traffic": 1000
      },
      {
        "name": "唯兔云 · 永久不限时 100GB",
        "price": 100,
        "billing": "One-Time",
        "traffic": 100
      },
      {
        "name": "唯兔云 · 永久不限时 200GB",
        "price": 160,
        "billing": "One-Time",
        "traffic": 200
      },
      {
        "name": "唯兔云 · 永久不限时 500GB",
        "price": 340,
        "billing": "One-Time",
        "traffic": 500
      }
    ]
  },
  "kuaili": {
    "file": "快狸",
    "lines": [
      "IEPL"
    ],
    "streaming": true,
    "ai": true,
    "promo": null,
    "nodeRegions": null,
    "plans": [
      {
        "name": "主推套餐",
        "price": 120,
        "billing": "Yearly",
        "traffic": 30
      },
      {
        "name": "月狸月付小套餐",
        "price": 15,
        "billing": "Monthly",
        "traffic": 50
      },
      {
        "name": "小狸基础版",
        "price": 22,
        "billing": "Monthly",
        "traffic": 100
      },
      {
        "name": "灵狸标准版",
        "price": 35,
        "billing": "Monthly",
        "traffic": 250
      },
      {
        "name": "夜狸强化版",
        "price": 95,
        "billing": "Monthly",
        "traffic": 500
      },
      {
        "name": "天狸顶配版",
        "price": 180,
        "billing": "Monthly",
        "traffic": 1024
      }
    ]
  },
  "xingdaomeng": {
    "file": "星岛梦",
    "lines": [
      "IPLC",
      "IEPL"
    ],
    "streaming": true,
    "ai": true,
    "promo": "nmw888",
    "nodeRegions": "香港×20、台湾×10、日本×10、新加坡×10、美国×10、韩国×2、阿根廷×2、马来西亚、越南、菲律宾、泰国、印度、德国、法国、英国等",
    "plans": [
      {
        "name": "星岛梦 · 贴心小包",
        "price": 96,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "星岛梦 · 超量150G",
        "price": 25,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "星岛梦 · 进阶300G",
        "price": 50,
        "billing": "Monthly",
        "traffic": 300
      },
      {
        "name": "星岛梦 · 闪光500G",
        "price": 70,
        "billing": "Monthly",
        "traffic": 500
      },
      {
        "name": "星岛梦 · 旗舰1T版",
        "price": 130,
        "billing": "Monthly",
        "traffic": 1000
      },
      {
        "name": "星岛梦 · 永久不限时100",
        "price": 100,
        "billing": "One-Time",
        "traffic": 100
      },
      {
        "name": "星岛梦 · 永久不限时300",
        "price": 300,
        "billing": "One-Time",
        "traffic": 300
      },
      {
        "name": "星岛梦 · 永久不限时1TB",
        "price": 600,
        "billing": "One-Time",
        "traffic": 1000
      },
      {
        "name": "星岛梦 · 定制套餐",
        "price": 680,
        "billing": "Monthly",
        "traffic": 500,
        "custom": true
      }
    ]
  },
  "muguang": {
    "file": "暮光",
    "lines": [
      "BGP"
    ],
    "streaming": true,
    "ai": true,
    "promo": "mm88",
    "nodeRegions": null,
    "plans": [
      {
        "name": "暮光 · 基础版",
        "price": 20,
        "billing": "Monthly",
        "traffic": 120
      },
      {
        "name": "暮光 · 标准版",
        "price": 40,
        "billing": "Monthly",
        "traffic": 240
      },
      {
        "name": "暮光 · 旗舰版",
        "price": 100,
        "billing": "Monthly",
        "traffic": 700
      },
      {
        "name": "暮光 · 至尊版",
        "price": 180,
        "billing": "Monthly",
        "traffic": 1500
      },
      {
        "name": "暮光 · 年付轻量版",
        "price": 109,
        "billing": "Yearly",
        "traffic": 70
      },
      {
        "name": "暮光 · 不限时轻量包",
        "price": 219,
        "billing": "One-Time",
        "traffic": 150
      },
      {
        "name": "暮光 · 不限时标准包",
        "price": 529,
        "billing": "One-Time",
        "traffic": 400
      },
      {
        "name": "暮光 · 不限时大容量包",
        "price": 959,
        "billing": "One-Time",
        "traffic": 800
      },
      {
        "name": "独享私人定制节点",
        "price": 600,
        "billing": "Monthly",
        "traffic": 500,
        "custom": true
      }
    ]
  },
  "jilian": {
    "file": "极连",
    "lines": [
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": "ji8888",
    "nodeRegions": "香港 x20、台湾 x10、日本 x10、新加坡 x10、马来西亚、美国 x10、泰国 x1、德国 x1、法国 x1、英国 x1、土耳其x1、韩国",
    "plans": [
      {
        "name": "限时年付套餐体验",
        "price": 96,
        "billing": "Yearly",
        "traffic": 60
      },
      {
        "name": "极连云 · 基础套餐",
        "price": 18,
        "billing": "Monthly",
        "traffic": 100
      },
      {
        "name": "极连云 · 进阶套餐",
        "price": 32,
        "billing": "Monthly",
        "traffic": 200
      },
      {
        "name": "极连云 · 旗舰套餐",
        "price": 61,
        "billing": "Monthly",
        "traffic": 500
      },
      {
        "name": "极连云 · 尊享套餐",
        "price": 122,
        "billing": "Monthly",
        "traffic": 1000
      },
      {
        "name": "极连云 · 不限时套餐",
        "price": 399,
        "billing": "One-Time",
        "traffic": 600
      }
    ]
  },
  "langwang": {
    "file": "浪网",
    "lines": [
      "BGP"
    ],
    "streaming": true,
    "ai": true,
    "promo": null,
    "nodeRegions": null,
    "plans": [
      {
        "name": "浪网 入门",
        "price": 30,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "浪网 进阶",
        "price": 70,
        "billing": "Monthly",
        "traffic": 400
      },
      {
        "name": "浪网 高端",
        "price": 120,
        "billing": "Monthly",
        "traffic": 800
      },
      {
        "name": "浪网 商业",
        "price": 200,
        "billing": "Monthly",
        "traffic": 2000
      },
      {
        "name": "浪网 年付标准",
        "price": 119,
        "billing": "Yearly",
        "traffic": 80
      },
      {
        "name": "浪网 小流量包",
        "price": 239,
        "billing": "One-Time",
        "traffic": 180
      },
      {
        "name": "浪网 标准流量包",
        "price": 569,
        "billing": "One-Time",
        "traffic": 450
      },
      {
        "name": "浪网 精英流量包",
        "price": 1099,
        "billing": "One-Time",
        "traffic": 900
      },
      {
        "name": "浪网 定制线路包",
        "price": 640,
        "billing": "Monthly",
        "traffic": 500,
        "custom": true
      }
    ]
  },
  "lingdong": {
    "file": "灵动",
    "lines": [
      "BGP"
    ],
    "streaming": true,
    "ai": true,
    "promo": "880223",
    "nodeRegions": null,
    "plans": [
      {
        "name": "灵动 · 拂风",
        "price": 20,
        "billing": "Monthly",
        "traffic": 100
      },
      {
        "name": "灵动 · 驭浪",
        "price": 50,
        "billing": "Monthly",
        "traffic": 300
      },
      {
        "name": "灵动 · 破晓",
        "price": 100,
        "billing": "Monthly",
        "traffic": 700
      },
      {
        "name": "灵动 · 凌霄",
        "price": 180,
        "billing": "Monthly",
        "traffic": 1500
      },
      {
        "name": "灵动 · 穿云",
        "price": 99,
        "billing": "Yearly",
        "traffic": 79
      },
      {
        "name": "灵动 · 闲云（小流量包）",
        "price": 199,
        "billing": "One-Time",
        "traffic": 150
      },
      {
        "name": "灵动 · 惊云（标准流量包）",
        "price": 499,
        "billing": "One-Time",
        "traffic": 400
      },
      {
        "name": "灵动 · 飞云（精英流量包）",
        "price": 899,
        "billing": "One-Time",
        "traffic": 800
      },
      {
        "name": "灵动云 · 至尊私人定制",
        "price": 620,
        "billing": "Monthly",
        "traffic": 500,
        "custom": true
      }
    ]
  },
  "sujie": {
    "file": "速界",
    "lines": [
      "IPLC"
    ],
    "streaming": true,
    "ai": true,
    "promo": null,
    "nodeRegions": "香港×20、台湾×10、日本×10、新加坡×10、美国×10、韩国×3、马来西亚、越南、泰国、英国、德国等",
    "plans": [
      {
        "name": "限时体验月付小包",
        "price": 15,
        "billing": "Monthly",
        "traffic": 50
      },
      {
        "name": "极速版",
        "price": 25,
        "billing": "Monthly",
        "traffic": 120
      },
      {
        "name": "超速版",
        "price": 50,
        "billing": "Monthly",
        "traffic": 250
      },
      {
        "name": "光速版",
        "price": 100,
        "billing": "Monthly",
        "traffic": 500
      },
      {
        "name": "跃迁版",
        "price": 200,
        "billing": "Monthly",
        "traffic": 1000
      },
      {
        "name": "限时年付",
        "price": 90,
        "billing": "Yearly",
        "traffic": 50
      }
    ]
  },
  "yinxingren": {
    "file": "隐形人",
    "lines": [
      "BGP"
    ],
    "streaming": true,
    "ai": true,
    "promo": null,
    "nodeRegions": null,
    "plans": [
      {
        "name": "白银纪元",
        "price": 24,
        "billing": "Monthly",
        "traffic": 144
      },
      {
        "name": "黄金序列",
        "price": 48,
        "billing": "Monthly",
        "traffic": 360
      },
      {
        "name": "铂金至尊",
        "price": 105,
        "billing": "Monthly",
        "traffic": 750
      },
      {
        "name": "钻石穹顶",
        "price": 185,
        "billing": "Monthly",
        "traffic": 1600
      },
      {
        "name": "一次性小流量",
        "price": 229,
        "billing": "One-Time",
        "traffic": 160
      },
      {
        "name": "一次性标准流量包",
        "price": 549,
        "billing": "One-Time",
        "traffic": 420
      },
      {
        "name": "一次性精英流量包",
        "price": 1199,
        "billing": "One-Time",
        "traffic": 1000
      }
    ]
  },
  "feiv": {
    "file": "飞v",
    "lines": [
      "IPLC",
      "BGP"
    ],
    "streaming": true,
    "ai": true,
    "promo": null,
    "nodeRegions": null,
    "plans": [
      {
        "name": "FlyV 年付标准轻量版",
        "price": 99,
        "billing": "Yearly",
        "traffic": 65
      },
      {
        "name": "FlyV 入门方案",
        "price": 25,
        "billing": "Monthly",
        "traffic": 150
      },
      {
        "name": "FlyV 进阶方案",
        "price": 50,
        "billing": "Monthly",
        "traffic": 380
      },
      {
        "name": "FlyV 高端方案",
        "price": 110,
        "billing": "Monthly",
        "traffic": 800
      },
      {
        "name": "FlyV 商业方案",
        "price": 190,
        "billing": "Monthly",
        "traffic": 1843.2
      },
      {
        "name": "FlyV 单次轻量版 · 小流量包",
        "price": 189,
        "billing": "One-Time",
        "traffic": 130
      },
      {
        "name": "FlyV 单次轻量版 · 标准流量包",
        "price": 479,
        "billing": "One-Time",
        "traffic": 380
      },
      {
        "name": "FlyV 单次轻量版 · 精英流量包",
        "price": 799,
        "billing": "One-Time",
        "traffic": 600
      },
      {
        "name": "FlyV 原生IP·独享黄金专线",
        "price": 600,
        "billing": "Monthly",
        "traffic": 500,
        "custom": true
      }
    ]
  }
};
