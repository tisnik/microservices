#!/usr/bin/env python3

import connexion
import time


def health_check():
    """Check the health status of the service."""
    return {}, 200


def get_readiness():
    """Get service readiness status."""
    print("begin")
    time.sleep(5)
    print("done")
    return health_check()


def get_liveness():
    """Get service liveness status."""
    print("begin")
    time.sleep(5)
    print("done")
    return health_check()


def main():
    """Start the Flask app."""
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'Service 5'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
