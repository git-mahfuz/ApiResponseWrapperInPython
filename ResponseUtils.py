import json
from multipledispatch import dispatch

class ResponseUtils:
	
	@dispatch(int)
	def apiResponse(code):
		return ResponseUtils.apiResponse(code, "", [], None)


	@dispatch(int,str)
	def apiResponse(code, message):
		return ResponseUtils.apiResponse(code, message, [], None)

	@dispatch(int,str,list)
	def apiResponse(code, message, errors):
		return ResponseUtils.apiResponse(code, message, errors, None)

	@dispatch(int,str,list,object)
	def apiResponse(code, message, errors, data = None):
		response = {
			"code": code,
			"message": message,
			"errors": errors,
			"data": data
		}

		return json.dumps(response)


print(ResponseUtils.apiResponse(400));
print(ResponseUtils.apiResponse(500, "Internal Server Error!"));
print(ResponseUtils.apiResponse(422, "Invalid Request", ["Username already exists", "Password must be at least 8 characters"]));
print(ResponseUtils.apiResponse(200, "Success!", [], None))