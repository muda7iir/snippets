import os

svg_1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="#e8f4f0"/><path d="M30 30 h40 v40 h-40 z" fill="none" stroke="#093322" stroke-width="4"/><path d="M40 45 h20 M40 55 h20 M40 65 h10" stroke="#c6a461" stroke-width="4" stroke-linecap="round"/></svg>'''

svg_2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="#e8f4f0"/><circle cx="50" cy="40" r="15" fill="none" stroke="#093322" stroke-width="4"/><path d="M30 80 c 0 -20 40 -20 40 0" fill="none" stroke="#093322" stroke-width="4"/><path d="M60 60 l 10 10 l 20 -20" fill="none" stroke="#c6a461" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

svg_3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="#e8f4f0"/><rect x="35" y="30" width="30" height="40" rx="5" fill="none" stroke="#093322" stroke-width="4"/><circle cx="50" cy="45" r="8" fill="#c6a461"/><path d="M40 60 h20" stroke="#093322" stroke-width="4" stroke-linecap="round"/></svg>'''

svg_4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="#e8f4f0"/><path d="M50 20 c -15 0 -25 10 -25 25 c 0 20 25 40 25 40 c 0 0 25 -20 25 -40 c 0 -15 -10 -25 -25 -25 z" fill="none" stroke="#093322" stroke-width="4"/><circle cx="50" cy="45" r="8" fill="#c6a461"/></svg>'''

watermark = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"><circle cx="100" cy="100" r="80" fill="none" stroke="#093322" stroke-width="2" opacity="0.1"/><circle cx="100" cy="100" r="60" fill="none" stroke="#c6a461" stroke-width="2" opacity="0.1"/></svg>'''

with open('process-icon-1.svg', 'w') as f: f.write(svg_1)
with open('process-icon-2.svg', 'w') as f: f.write(svg_2)
with open('process-icon-3.svg', 'w') as f: f.write(svg_3)
with open('process-icon-4.svg', 'w') as f: f.write(svg_4)
with open('process-watermark.svg', 'w') as f: f.write(watermark)
