from fastapi import Request, Response
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from jinja2 import Environment, PackageLoader, select_autoescape

from app import config

env = Environment(
    loader=PackageLoader("app", "templates"),
    autoescape=select_autoescape(["html", "xml"])
)


async def send_mail(request: Request, response: Response,
                    email_data):

    conf = config.get_mail_config()

    mail_config = ConnectionConfig(
        MAIL_USERNAME=conf.mail_username,
        MAIL_PASSWORD=conf.mail_password,
        MAIL_PORT=conf.mail_port,
        MAIL_SERVER=conf.mail_server,
        MAIL_STARTTLS=conf.mail_tls,
        MAIL_SSL_TLS=conf.mail_ssl_tls,
        MAIL_FROM=conf.mail_from
    )

    template = env.get_template("email.html")
    html = template.render(
        title="Fuzzy Link",
        link=request.cookies.get("fuzzy_url")
    )

    message = MessageSchema(
        subject="Fuzzy Link",
        recipients=email_data.dict().get("email"),
        body=html,
        subtype="html"
    )

    fm = FastMail(mail_config)
    await fm.send_message(message=message)
    print(message)

    response.delete_cookie("fuzzy_url")

    return {
        "message": "success"
    }
