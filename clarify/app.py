from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from tags import get_relevant_tags


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms_reply():
    # Create a MessagingResponse object to generate TwiML.
    resp = MessagingResponse()

    # See if the number of images in the text message is greater than zero.
    if request.form['NumMedia'] != '0':

        # Grab the image URL from the request body.
        image_url = request.form['MediaUrl0']
        relevant_tags = get_relevant_tags(image_url)
        resp.message('n'.join(relevant_tags))
    else:
        resp.message('Please send an image.')

    return str(resp)


if __name__ == '__main__':
    app.run()
