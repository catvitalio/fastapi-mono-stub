from fastapi_mail import MessageSchema, MessageType

from config.mail import mail
from config.taskiq import broker


@broker.task
async def send_mail(subject: str, template: str, context: dict, recipients: list[str]) -> None:
    schema = MessageSchema(
        subject=subject,
        recipients=recipients,
        template_body=context,
        subtype=MessageType.html,
    )
    await mail.send_message(schema, template_name=template)
