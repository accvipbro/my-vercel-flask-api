from flask import Flask, request, jsonify

app = Flask(__name__)

request_count = 0

@app.route('/api/add_request', methods=['POST'])
def add_tiktok_request():
    global request_count

    # Bỏ comment hoặc thêm dòng này để sử dụng request
    data = request.get_json() # Ví dụ: lấy dữ liệu JSON từ body của request
    # print(f"Received data: {data}") # In ra để kiểm tra

    request_count += 1

    return jsonify({
        'status': 'success',
        'message': 'Request added successfully',
        'current_request_count': request_count
    })

# ... các phần còn lại của code