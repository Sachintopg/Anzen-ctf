from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for validating the payload
@app.route('/validate', methods=['POST'])
def validate_payload():
    data = request.json
    
    # Check for the exact match of '-alert(xss)-'
    correct_payload = '-alert(1)-'
    
    if data and data['payload'].strip() == correct_payload:
        flag = "Anzen CTF{alert}"
        return jsonify({"valid": True, "flag": flag})
    else:
        return jsonify({"valid": False})

if __name__ == '__main__':
    app.run(debug=True)
