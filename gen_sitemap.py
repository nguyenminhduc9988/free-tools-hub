import os, datetime

tools = sorted([f for f in os.listdir('tools') if f.endswith('.html')])
base = 'https://nguyenminhduc9988.github.io/free-tools-hub'
today = datetime.date.today().isoformat()

lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
lines.append(f'  <url><loc>{base}/</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>')
for t in tools:
    slug = t.replace('.html', '')
    lines.append(f'  <url><loc>{base}/tools/{slug}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>')
lines.append('</urlset>')

with open('sitemap.xml', 'w') as f:
    f.write('\n'.join(lines))

print(f"Sitemap generated: 1 homepage + {len(tools)} tools = {len(tools)+1} URLs")
