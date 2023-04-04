import re

def detect_code(text):
    patterns = {
        'Python': [
            r'\b(def|class)\s+\w+\(',
            r'\b(lambda)\s+(.*?):\s+(.*)',
        ],
        'Java': [
            r'for\s*\(\s*(?:[a-zA-Z_]\w*\s+)?([a-zA-Z_]\w*)\s*:\s*([^\{\};]+)\s*\)\s*\{'
            r'\b(public|private|protected)\s+class\s+(\w+)\s*([^{]*)\{',
            r'\b(public|private|protected)\s+class\s+\w+\s*{',
            r'\b(new)\s+\w+\(',
        ],
        'C': [
            r'\b(int|float|double|char|void)\s+\w+\s*\(',
            r'\b(return)\s+\w+\s*;',
        ],
        'C#': [
            r'\b(public|private|protected)\s+class\s+\w+\s*{',
        ],
        'Go': [
            r'\b(func)\s+\w+\(',
        ],
        'Javascript': [
            r'\b(function)\s+\w*\s*\(',
        ],
        'R': [
            r'\b(function)\s*\(.*?\)\s*{',
        ],
        'Ruby': [
            r'\b(def|class)\s+\w+',
        ],
        'PHP': [
            r'\b(function)\s+\w+\(',
        ],
        'Swift': [
            r'\b(func)\s+\w+\(',
        ],
        'Kotlin': [
            r'\b(fun)\s+\w+\(',
        ],
        'Scala': [
            r'\b(def)\s+\w+\(',
        ],
        'Objective-C': [
            r'\b(-|\+)\s+\([a-zA-Z]*\)\w+',
        ],
        'SwiftUI': [
            r'\.body\s*\{',
        ],
        'React': [
            r'render\s*\(',
        ],
        'Vue': [
            r'template\s*:\s*`',
        ],
        'Angular': [
            r'@Component\s*\(',
        ],
        'Django': [
            r'from\s+django\.',
        ],
        'Flask': [
            r'from\s+flask\.',
        ],
        'Rails': [
            r'rails\s+generate\s+',
        ],
        'Express': [
            r'const\s+express\s*=\s*require\s*\(',
        ],
        'Laravel': [
            r'Illuminate\\',
        ],
        'Spring': [
            r'import\s+org\.springframework\.',
        ],
        'Hibernate': [
            r'import\s+org\.hibernate\.',
        ],
        'SQL': [
            r'\b(SELECT|FROM|WHERE|GROUP BY|ORDER BY)\s+.*',
        ],
        'MATLAB': [
            r'\b(function)\s+\w+\s*\(.*?\)',
        ],
        'E-Mail' : [
            r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*',
        ],
        'URL' : [
            r'((http|https|ftp):\/\/)?([a-z0-9]+(\.[a-z0-9]+)*\.[a-z]{2,6})(:[0-9]{1,4})?(\/.*)?',
        ],
        # 可以添加其他语言的正则表达式
    }
    for lang, patterns_list in patterns.items():
        for pattern in patterns_list:
            if re.search(pattern, text):
                return lang, text
    return None, text