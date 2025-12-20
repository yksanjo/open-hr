"""CLI for OpenHR."""

import click
import json
from .framework import AgentFramework, Agent


@click.group()
def cli():
    """OpenHR - Open-Source HR Agent Platform."""
    pass


@cli.command()
def list_agents():
    """List available agents."""
    framework = AgentFramework()
    agents = framework.list_agents()
    
    if agents:
        click.echo("🤖 Available Agents:\n")
        for agent in agents:
            click.echo(f"  - {agent['name']} (v{agent['version']})")
    else:
        click.echo("No agents registered. Use 'open-hr register' to add agents.")


@cli.command()
@click.option("--agent-name", required=True, help="Agent name")
@click.option("--task", required=True, help="Task JSON string")
def execute(agent_name: str, task: str):
    """Execute an agent."""
    framework = AgentFramework()
    task_dict = json.loads(task)
    
    try:
        result = await framework.execute_agent(agent_name, task_dict)
        click.echo(json.dumps(result, indent=2))
    except ValueError as e:
        click.echo(f"❌ Error: {e}", err=True)


@cli.command()
def marketplace():
    """Show agent marketplace."""
    click.echo("🏪 OpenHR Agent Marketplace\n")
    click.echo("Available Agents:")
    click.echo("  1. Recruiting Agent - Automated candidate sourcing")
    click.echo("  2. Onboarding Agent - New hire automation")
    click.echo("  3. Payroll Agent - Payroll processing")
    click.echo("  4. Benefits Agent - Benefits management")
    click.echo("\n💡 Contribute your own agents at: https://github.com/openhr/agents")


if __name__ == "__main__":
    cli()

