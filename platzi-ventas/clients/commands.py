import click

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """ Manages the clients lifecycle """
    pass


@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The client name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-j', '--job',
              type=str,
              prompt=True,
              help='The client job')
@click.pass_context
def create(ctx, name, company, email, job):
    """ Creates a new client """
    click.echo(ctx)
    client = Client(name, company, email, job)
    client_services = ClientService(ctx.obj['clients_table'])

    client_services.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """ List all clients """
    client_service = ClientService(ctx.obj['clients_table'])

    clients_list = client_service.list_clients()

    click.echo('ID  |  NAME  |  COMPANY  |  EMAIL  |  JOB  ')
    click.echo('*' * 100)
    for client in clients_list:
        click.echo('{uid}  |  {name} |  {company}  |  {email}  |  {job}'.format(
                                                                            uid=client['uid'],
                                                                            name=client['name'],
                                                                            company=client['company'],
                                                                            email=client['email'],
                                                                            job=client['job']
                                                                        ))


@clients.command()
@click.argument('client_uid',type=str)
@click.pass_context
def update(ctx, client_uid):
    """ Update a client """
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Cliente updated')
    else:
        click.echo('Client not found')


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
    """ Delete a client """
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()

    client = [client for client in client_list if client['uid'] == client_uid]
    
    if client:
        client_service.delete_client(client)

        click.echo('Cliente deleted')
    else:
        click.echo('Client not found')



def _update_client_flow(client):
    click.echo('Leave empty if you don\'t want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.job = click.prompt('New job', type=str, default=client.job)

    return client


all = clients
