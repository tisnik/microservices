#!/usr/bin/env python3

import connexion
from collections import Counter


def health_check():
    """Check the health status of the service."""
    return {}, 200


def get_readiness():
    """Get service readiness status."""
    return health_check()


def get_liveness():
    """Get service liveness status."""
    return health_check()


KNOWN_RECIPIENTS = {"Puchmajer", "Meyer", "Pihrt", "Jason", "Drson", "Trachta", "Fristensky"}
ALLOWED_RECIPIENTS = {"Jason", "Drson", "Trachta", "Fristensky"}

counter = Counter()


def send_message(recipient, message):
    """Send a message to selected recipient."""
    if not recipient:
        return {"Status": "error",
                "Reason": "No recipient supplied"}, 400

    if not message:
        return {"Status": "error",
                "Reason": "Message is empty"}, 400

    if recipient not in KNOWN_RECIPIENTS:
        return {"Status": "not found",
                "Reason": "The specified recipient was not found"}, 404

    if recipient not in ALLOWED_RECIPIENTS:
        return {"Status": "forbidden",
                "Reason": "Not allowed - it is not allowed to send the message to selected recipient"}, 405

    try:
        # kod pro skutecne poslani zpravy
        counter[recipient] += 1
        return {"Status": "ok"}, 200
    except Exception as e:
        return {"Status": "error", "Reason": str(e)}, 500


def message_statistic():
    """Returns message statistic."""
    return counter


def main():
    """Start the Flask app."""
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'Service 3'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
