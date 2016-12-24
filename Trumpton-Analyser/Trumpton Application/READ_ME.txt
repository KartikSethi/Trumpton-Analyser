The application requires various conda packages whose support is not provided by heroku.
'packages_to_be_installed.txt' contains the list of packages required for successfully running the application on a local machine. 

To run the application one just need to run the 'app.py' file. Since my classification model is trained using Keras, it might look for GPU presence on the system.
Once the code is executed, the user can open the web browser and type in 'localhost:5000' to open app page.
