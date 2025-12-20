"""Open-source agent framework."""

from typing import Dict, Any, List
from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class Agent(ABC):
    """Base agent interface."""
    
    def __init__(self, name: str, version: str = "1.0.0"):
        self.name = name
        self.version = version
        self.agent_id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
    
    @abstractmethod
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute agent task."""
        pass


class AgentFramework:
    """Open-source agent framework."""
    
    def __init__(self):
        self.agents: Dict[str, Agent] = {}
    
    def register_agent(self, agent: Agent):
        """Register an agent."""
        self.agents[agent.name] = agent
    
    def list_agents(self) -> List[Dict[str, Any]]:
        """List all registered agents."""
        return [
            {
                "name": agent.name,
                "version": agent.version,
                "agent_id": agent.agent_id
            }
            for agent in self.agents.values()
        ]
    
    async def execute_agent(self, agent_name: str, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute an agent."""
        if agent_name not in self.agents:
            raise ValueError(f"Agent {agent_name} not found")
        
        agent = self.agents[agent_name]
        return await agent.execute(task)

