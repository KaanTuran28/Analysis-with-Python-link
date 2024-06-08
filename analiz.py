from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
    <body>
    <h1>Kullanıcı Bilgi Kaydetme</h1>
    <p>Bu uygulama, tarayıcı üzerinden otomatik olarak kullanıcı bilgilerini kaydediyor.</p>
    </body>
    </html>
    '''

@app.before_request
def before_request():
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    referer = request.headers.get('Referer')
    accept_language = request.headers.get('Accept-Language')
    screen_resolution = request.headers.get('Screen-Resolution')
    color_depth = request.headers.get('Color-Depth')
    browser = request.user_agent.browser
    browser_version = request.user_agent.version
    platform = request.user_agent.platform
    remote_host = request.headers.get('X-Remote-Host')
    forwarded_for = request.headers.get('X-Forwarded-For')
    content_type = request.headers.get('Content-Type')
    content_length = request.headers.get('Content-Length')
    connection = request.headers.get('Connection')
    cache_control = request.headers.get('Cache-Control')

    with open("user_info.txt", "a") as file:
        if user_agent:
            file.write("User Agent: {}\n".format(user_agent))
        if ip_address:
            file.write("IP Address: {}\n".format(ip_address))
        if referer:
            file.write("Referer: {}\n".format(referer))
        if accept_language:
            file.write("Accept-Language: {}\n".format(accept_language))
        if screen_resolution:
            file.write("Screen Resolution: {}\n".format(screen_resolution))
        if color_depth:
            file.write("Color Depth: {}\n".format(color_depth))
        if browser:
            file.write("Browser: {}\n".format(browser))
        if browser_version:
            file.write("Browser Version: {}\n".format(browser_version))
        if platform:
            file.write("Platform: {}\n".format(platform))
        if remote_host:
            file.write("Remote Host: {}\n".format(remote_host))
        if forwarded_for:
            file.write("Forwarded For: {}\n".format(forwarded_for))
        if content_type:
            file.write("Content Type: {}\n".format(content_type))
        if content_length:
            file.write("Content Length: {}\n".format(content_length))
        if connection:
            file.write("Connection: {}\n".format(connection))
        if cache_control:
            file.write("Cache Control: {}\n".format(cache_control))

        file.write("\n")

@app.route('/save_info')
def save_info():
    return '''
    <html>
    <body>
    <h1>Bilgiler başarıyla kaydedildi!</h1>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
