#!/usr/bin/env python3

import connexion


def main():
    """Start the Flask app."""
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'Service 1'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
