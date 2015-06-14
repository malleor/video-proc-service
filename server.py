from bottle import run, route, redirect, static_file
from sys import argv


if __name__ == "__main__":
    # prep data

    # set up client route
    @route('/')
    def home():
        # respond
        return redirect('/index.htm')

    @route('/<filename:path>')
    def send_static(filename):
        return static_file(filename, root='./static/')
    
    # set up processing route
    @route('/proc')
    def process_video():
        pass

    # run the server
    run(host='0.0.0.0', port=argv[1])
