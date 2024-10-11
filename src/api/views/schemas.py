from flask_restx import fields, Model


index_model = Model(
    "Health-Status",
    {
        "service": fields.String(
            description="Service name"
        ),
        "version": fields.String(
            description="API version"
        )
    }
)

generic_response_model = Model(
    "GenericResponse",
    {
        "code": fields.String(example="ABC900"),
        "message": fields.String(example="Generic message")
    }
)


token_request_model = Model(
    "Token request",
    {
        "username": fields.String(
            description="Username"
        ),
        "password": fields.String(
            description="Password"
        )
    }
)


token_response_model = Model(
    "Token Response",
    {
        "token": fields.String(
            description="token"
        )
    }
)


authorization_header = {
    "Authorization": fields.String(
        description="Authorization: Bearer"
    )
}
