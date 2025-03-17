from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Dataassistant():
	"""Dataassistant crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	data_agents_config = 'config/data_agents.yaml'
	data_tasks_config = 'config/data_tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def senior_product_manager(self) -> Agent:
		return Agent(
			config=self.data_agents_config['senior_product_manager'],
			verbose=True
		)

	@agent
	def senior_data_engineer(self) -> Agent:
		return Agent(
			config=self.data_agents_config['senior_data_engineer'],
			verbose=True
		)

	@agent
	def senior_data_engineer_manager(self) -> Agent:
		return Agent(
			config=self.data_agents_config['senior_data_engineer_manager'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def understand_requirement_task(self) -> Task:
		return Task(
			config=self.data_tasks_config['understand_requirement_task'],
		)

	@task
	def write_query_task(self) -> Task:
		return Task(
			config=self.data_tasks_config['write_query_task']
		)
	
	@task
	def code_review_task(self) -> Task:
		return Task(
			config=self.data_tasks_config['code_review_task']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Dataassistant crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
