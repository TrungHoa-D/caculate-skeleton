import re

# Read file
with open('iPhone Air - Apple (VN).html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the inline style block that disables animations
# Pattern: <style> ... Force hiển thị ảnh fallback ... </style>
pattern = r'<style>\s*\n\s*/\* Force hiển thị ảnh fallback.*?</style>'

if re.search(pattern, content, re.DOTALL):
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    print("SUCCESS: Removed inline CSS block that disables animations")
else:
    # Try simpler pattern
    pattern2 = r'<style>\s*\n\s*/\* Force hiển thị'
    if pattern2[:30] in content:
        # Find start and end positions
        start_marker = '  <style>\n    /* Force hiển thị ảnh fallback'
        end_marker = '</style>\n</head>'
        
        idx1 = content.find('/* Force hiển thị ảnh fallback')
        if idx1 > 0:
            # Find the <style> before this comment
            style_start = content.rfind('<style>', 0, idx1)
            # Find </style> after
            style_end = content.find('</style>', idx1) + len('</style>')
            
            if style_start > 0 and style_end > style_start:
                removed = content[style_start:style_end]
                content = content[:style_start] + content[style_end:]
                print(f"SUCCESS: Removed {len(removed)} characters of inline CSS")
    else:
        print("WARNING: Could not find the inline style block")

# Write file
with open('iPhone Air - Apple (VN).html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved!")
