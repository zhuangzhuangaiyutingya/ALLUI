import streamlit as st
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="哇！的资料分享",
    page_icon="📄",
    layout="centered"
)

# 简约样式
st.markdown("""
<style>
    h1 {
        color: #3498db;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .link-card {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 6px;
        margin-bottom: 0.8rem;
        border-left: 3px solid #3498db;
    }
    .link-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #3498db;
        margin-bottom: 0.3rem;
    }
    .link-url {
        color: #555;
        font-size: 0.9rem;
        word-break: break-all;
    }
    .link-desc {
        color: #666;
        margin: 0.5rem 0;
    }
    .link-meta {
        color: #888;
        font-size: 0.8rem;
    }
    .btn-add {
        background-color: #3498db;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# 初始化示例链接
if 'links' not in st.session_state:
    st.session_state.links = [
        {
            'title': 'YOLO一键运行模板',
            'url': 'https://pan.baidu.com/s/1qGhZMA8RCjO3eu3_SyI8hw?pwd=wzzz',
            'description': '替换数据集一键运行',
            'date': '2025-04-24',
            'category': '程序'
        }
    ]

# 页面标题
st.markdown("<h1>📄 哇！的资料分享</h1>", unsafe_allow_html=True)


# 搜索框
search = st.text_input("搜索资料", placeholder="输入关键词...")

# 分类筛选（如果需要）
all_categories = sorted(list(set([link['category'] for link in st.session_state.links])))
if all_categories:
    selected_category = st.selectbox("按分类筛选", ["全部"] + all_categories)
else:
    selected_category = "全部"

# 筛选链接
filtered_links = st.session_state.links
if search:
    filtered_links = [
        link for link in filtered_links
        if search.lower() in link['title'].lower()
           or search.lower() in link['description'].lower()
           or search.lower() in link['url'].lower()
    ]

if selected_category != "全部":
    filtered_links = [link for link in filtered_links if link['category'] == selected_category]

# 显示链接列表
if not filtered_links:
    st.info("没有找到相关资料链接")

for link in filtered_links:
    st.markdown(f"""
    <div class="link-card">
        <div class="link-title">{link['title']}</div>
        <a href="{link['url']}" target="_blank" class="link-url">{link['url']}</a>
        <p class="link-desc">{link['description']}</p>
        <div class="link-meta">
            {link['category']} · 添加于 {link['date']}
        </div>
    </div>
    """, unsafe_allow_html=True)

# 添加页脚
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888; padding: 1rem 0;'>"
    "联系作者：抖音wzz1.0"
    "</div>",
    unsafe_allow_html=True
)