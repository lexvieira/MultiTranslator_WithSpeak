from app.main import app
import os
# app.run(host='0.0.0.0', port=os.environ.get('PORT', default=5000))
if __name__ == 'main':
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))