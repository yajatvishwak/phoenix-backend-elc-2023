# Phoenix -- Backend

This repo holds the backend code for the Phoenix accessibilty platform build for the ELC Hackathon 2023.

I've used a python flask server that exposes APIs to interact with the frontend application.

This prototype application showcases an innovative approach to improving the accessibility of online e-commerce platforms, particularly in the beauty industry, through the integration of cutting-edge technologies such as voice control and computer vision. By leveraging these advanced tools, users can enjoy a more seamless and intuitive shopping experience that caters to a wide range of needs and preferences.

While some common features such as sign up, sign in, and multi-user support have not been included in this prototype, this intentional omission underscores the project's primary focus on exploring novel ways to leverage AI to enhance accessibility. By prioritizing the development of a sophisticated AI bot experience, this prototype represents a significant step forward in advancing the state of the art in e-commerce accessibility and creating more inclusive online environments for all users.

To install,

1. Create an `.env` file
2. In the `.env` file, add `PHONE=XXXXXXXXXX`
3. Create folders at source level, `justfaces`, `uploads`, `makeup_iamges` 
3. `python3 venv -m env && source ./env/bin/activate `
4. Install dependencies,  `pip install -r requirements.txt`
5. `python server.py`
6. Check if server is online by visiting `http://localhost:5000`


Prototype Backend building specs requirements:
1. Minimum of 16GB RAM
2. Ubuntu 20.04 - (could use other platforms, but haven't tested it out)
3. python 3.8.10
4. Minimum 10 GB of available storage
