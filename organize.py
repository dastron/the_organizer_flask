from the_organizer.webapp import *
api = setup_app(os.getenv('ORGANIZER_CONFIG', 'default'), app, database)

if __name__ == '__main__':
    app.run()
