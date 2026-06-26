import yaml
from pathlib import Path
from crewai import Agent, Task, Crew, Process, BaseAgent
from crewai.project import CrewBase, agent, crew, task
from mardown_validator.tools.markdowntool import markdown_validation_tool

@CrewBase
class MarkDownValidatorCrew:
    agents_config = yaml.safe_load(Path('config/agents.yaml').read_text())
    tasks_config = yaml.safe_load(Path('config/tasks.yaml').read_text())
    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def RequirementsManager(self) -> Agent:
        return Agent(
            config=self.agents_config['Requirements_Manager'],
            tools=[markdown_validation_tool],
            allow_delegation=False,
            verbose=False
        )

    @task
    def syntax_review_task(self) -> Task:
        return Task(
            description="Review markdown file syntax",
            expected_output="A detailed markdown syntax validation report",
            config=self.tasks_config['syntax_review_task'],
            agent=self.RequirementsManager
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MarkDownValidatorCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=False,
        )