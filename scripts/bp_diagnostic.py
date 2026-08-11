#!/usr/bin/env python3
"""
BP 叙事框架诊断脚本

扫描一个 Markdown 格式的 BP 文档，检查三核心问题与六支柱是否被覆盖。
用法：
    python bp_diagnostic.py /path/to/your-bp.md
"""

import argparse
import re
import sys
from pathlib import Path


def read_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"找不到文件: {path}")
    return p.read_text(encoding="utf-8")


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text.lower())


def check_pillars(text: str) -> dict:
    normalized = normalize(text)

    checks = {
        "Q1 不可逆趋势 / Timing": {
            "keywords": ["为什么是现在", "时机", "timing", "不可逆趋势", "临界点", "拐点", "基础设施"],
            "required": 1,
        },
        "Q2 非你不可 / Who&Why": {
            "keywords": ["为什么是我们", "为什么是你", "非你不可", "创始人", "团队", "过往", "独家数据", "渠道", "壁垒"],
            "required": 1,
        },
        "Q3 风险递减路径 / Proof Points": {
            "keywords": ["风险", "里程碑", "milestone", "验证", "proof", "留存", "毛利", "回本周期"],
            "required": 1,
        },
        "支柱一 Timing": {
            "keywords": ["timing", "时机", "成本拐点", "性能拐点", "需求临界点", "监管窗口"],
            "required": 1,
        },
        "支柱二 Vision": {
            "keywords": ["终局", "vision", "细分场景", "扩张路径", "tam", "sam", "sorm", "单位经济"],
            "required": 1,
        },
        "支柱三 Who&Why": {
            "keywords": ["founder", "使命", "洞察", "不对称优势", "客户背书", "技术原型", "人才磁场"],
            "required": 1,
        },
        "支柱四 Moat": {
            "keywords": ["护城河", "moat", "网络效应", "切换成本", "生态", "标准", "协议", "边际成本"],
            "required": 1,
        },
        "支柱五 Scale": {
            "keywords": ["scale", "规模化", "复制", "标准化", "平台", "获客成本", "cac", "ltv", "nrr"],
            "required": 1,
        },
        "支柱六 Proof Points": {
            "keywords": ["里程碑", "验证点", "proofpoints", "性能超越", "次月留存", "付费客户", "假设"],
            "required": 1,
        },
    }

    results = {}
    for pillar, cfg in checks.items():
        hits = sum(1 for kw in cfg["keywords"] if kw.lower().replace(" ", "") in normalized)
        results[pillar] = {
            "hits": hits,
            "keywords": cfg["keywords"],
            "passed": hits >= cfg["required"],
        }
    return results


def render_report(results: dict, filename: str) -> str:
    lines = [f"# BP 叙事框架诊断报告\n", f"源文件: {filename}\n"]
    lines.append("| 维度 | 命中关键词数 | 状态 |\n")
    lines.append("|------|-------------|------|\n")

    passed = 0
    for pillar, info in results.items():
        status = "✅ 已覆盖" if info["passed"] else "❌ 未覆盖 / 覆盖不足"
        lines.append(f"| {pillar} | {info['hits']} | {status} |\n")
        if info["passed"]:
            passed += 1

    total = len(results)
    lines.append(f"\n覆盖度: {passed}/{total} ({passed / total * 100:.0f}%)\n")

    missing = [p for p, i in results.items() if not i["passed"]]
    if missing:
        lines.append("\n## 建议优先补强的维度\n")
        for p in missing:
            lines.append(f"- **{p}**\n")

    return "".join(lines)


def main():
    parser = argparse.ArgumentParser(description="诊断 BP Markdown 是否覆盖六支柱叙事框架")
    parser.add_argument("file", help="待诊断的 Markdown 文件路径")
    args = parser.parse_args()

    text = read_file(args.file)
    results = check_pillars(text)
    report = render_report(results, args.file)
    print(report)

    return 0


if __name__ == "__main__":
    sys.exit(main())
