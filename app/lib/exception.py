from flask import got_request_exception, jsonify

def init(app):
    got_request_exception.connect(log_exception, app)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(500, handle_500)
    

def handle_404(e):
    return jsonify({'message': 'Not Found'}), 404 

def handle_500(e):
    return jsonify({'message': 'Internal Server Error'}), 500

def log_exception(sender, exception, **extra):
    print('Got exception during processing: %s', exception)


