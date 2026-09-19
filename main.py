import json
import math
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class CalculatorRequestHandler(SimpleHTTPRequestHandler):
	def do_POST(self):
		if self.path != "/add":
			self.send_error(404, "ไม่พบ endpoint นี้")
			return

		try:
			content_length = int(self.headers.get("Content-Length", 0))
			request_data = json.loads(self.rfile.read(content_length))
			first_number = float(request_data["first"])
			second_number = float(request_data["second"])
			if not math.isfinite(first_number) or not math.isfinite(second_number):
				raise ValueError
		except (KeyError, TypeError, ValueError, json.JSONDecodeError):
			self.send_error(400, "กรุณาส่งตัวเลขที่ถูกต้อง")
			return

		response_data = {"result": first_number + second_number}
		response_body = json.dumps(response_data).encode("utf-8")
		self.send_response(200)
		self.send_header("Content-Type", "application/json; charset=utf-8")
		self.send_header("Content-Length", str(len(response_body)))
		self.end_headers()
		self.wfile.write(response_body)


if __name__ == "__main__":
	server = ThreadingHTTPServer(("localhost", 8000), CalculatorRequestHandler)
	print("เปิดเว็บได้ที่ http://localhost:8000")
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		print("\nหยุดการทำงานของเซิร์ฟเวอร์")
	finally:
		server.server_close()