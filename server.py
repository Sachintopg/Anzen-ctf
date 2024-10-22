from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for validating the payload
@app.route('/validate', methods=['POST'])
def validate_payload():
    data = request.json
    
    # Check for the exact match of '-alert(xss)-'
    correct_payload = '-alert(xss)-'
    
    if data and data['payload'].strip() == correct_payload:
        try:
            # Execute the payload as JavaScript code
            eval(data['payload'])
            flag = "Anzen CTF{alert}"
            return jsonify({"valid": True, "flag": flag})
        except Exception as e:
            return jsonify({"valid": False, "error": str(e)})
    else:
        return jsonify({"valid": False})

if __name__ == '__main__':
    app.run(debug=True)