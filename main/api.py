from rest_framework.response import Response
from rest_framework.views import APIView


class FaceDetectionAPI(APIView):
    """
    Input: Image
    Output: Accept / Reject & Fitment score
    """

    def post(self, request, format=None):
        print(request.data['image'])
        return Response({"Status": "SUCCESS"})
