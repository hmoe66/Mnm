from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# تخزين الأوامر بسرعة فائقة
current_command = {"action": "none", "value": ""}

# واجهة العرض الرئيسية (الداتا شو - الأداء الخارق والألعاب)
DISPLAY_HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Gaming & Media Pro - Ultra Fast</title>
    <style>
        * { box-sizing: border-box; }
        body { background: #0b0b0f; color: #fff; font-family: 'Segoe UI', Tahoma, sans-serif; margin: 0; padding: 15px; text-align: center; overflow-x: hidden; }
        h1 { color: #00ffcc; font-size: 2.2rem; margin: 5px 0 15px 0; text-shadow: 0 0 10px rgba(0,255,204,0.3); }
        .grid-container { display: grid; grid-template-columns: 2fr 1fr; gap: 20px; max-width: 1400px; margin: 0 auto; }
        .panel { background: #14141c; padding: 15px; border-radius: 12px; border: 1px solid #22223b; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        iframe { width: 100%; height: 450px; border-radius: 8px; border: none; background: #000; }
        .games-list { display: grid; grid-template-columns: 1fr; gap: 10px; max-height: 450px; overflow-y: auto; }
        .game-btn { background: #1f1f2e; color: #fff; border: 1px solid #33334d; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; transition: all 0.2s ease; text-align: right; }
        .game-btn:hover { background: #00ffcc; color: #000; border-color: #00ffcc; transform: translateY(-2px); }
        #ping-status { margin-top: 10px; font-size: 1rem; color: #00ffcc; background: #121218; padding: 8px; border-radius: 6px; display: inline-block; border: 1px solid #1f1f2e; }
    </style>
</head>
<body>
    <h1>⚡ نظام الألعاب والترفيه الخارق (Ultra Fast)</h1>
    <div id="ping-status">النظام متصل وجاهز للأوامر السريعة...</div>
    
    <div class="grid-container" style="margin-top: 15px;">
        <div class="panel">
            <h3 style="margin-top:0; color:#ff0055;">🎥 شاشة التشغيل واللعب الرئيسية</h3>
            <iframe id="main-frame" src="https://www.youtube.com/embed/5qap5aO4i9A?enablejsapi=1" allowfullscreen></iframe>
        </div>
        <div class="panel">
            <h3 style="margin-top:0; color:#00ffcc;">🎮 منصة الألعاب السريعة</h3>
            <div class="games-list">
                <div class="game-btn" onclick="launchGame('https://pacman.live/')">🟡 باكمان الأسطورية (Pacman)</div>
                <div class="game-btn" onclick="launchGame('https://tetris.com/play-tetris')">🧱 تترس الكلاسيكية (Tetris)</div>
                <div class="game-btn" onclick="launchGame('
