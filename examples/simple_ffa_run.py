'''An example to show how to set up an pommerman game programmatically'''
import pommerman
from pommerman import agents

from pommerman.agents import TensorForceAgent

def main():
    '''Simple function to bootstrap a game.
       
       Use this as an example to set up your training env.
    '''
    # Print all possible environments in the Pommerman registry
    print(pommerman.REGISTRY)

    # Create a set of agents (exactly four)
    agent_list = [
        agents.TensorForceAgent(),
        agents.SimpleAgent(),
        agents.SimpleAgent(),
        agents.SimpleAgent(),
        # agents.SimpleAgent(),
        # agents.RandomAgent(),
        # agents.PlayerAgent(),
        # agents.DockerAgent("pommerman/simple-agent", port=12345),
    ]
    # Make the "Free-For-All" environment using the agent list
    # env = pommerman.make('PommeFFACompetitionFast-v0', agent_list)
    env = pommerman.make('PommeTeamCompetition-v0', agent_list)

    # Initialize already trained agent model
    for agent in agent_list:
        i = 0
        if type(agent) == TensorForceAgent:
            agent.initialize(env)
            print('trained agent[{}] initiazlied.'.format(type(agent)))
        else:
            print('simple agent[{}] initiazlied.'.format(type(agent)))

    # Run the episodes just like OpenAI Gym
    for i_episode in range(1):
        state = env.reset()
        done = False
        while not done:
            env.render()
            actions = env.act(state)
            state, reward, done, info = env.step(actions)
        print('Episode {} finished'.format(i_episode))
    env.close()


if __name__ == '__main__':
    main()
