from gym.envs.registration import register

register(id="Continuous-v0", entry_point="driving.envs:GridworldContinuousEnv")
# register(id="ContinuousRandom-v0", entry_point="driving.envs:GridworldContinuousRandomInitEnv")
# register(id="ContinuousRandom1-v0", entry_point="driving.envs:GridworldContinuousRandomInitEnv1",max_episode_steps=400)
# register(id="ContinuousLeftRandom1-v0", entry_point="driving.envs:GridworldContinuousLeftRandomInitEnv1")
# register(id="ContinuousRightRandom1-v0", entry_point="driving.envs:GridworldContinuousRightRandomInitEnv1")
register(id="ContinuousFastRandom-v0", entry_point="driving.envs:GridworldContinuousFastRandomInitEnv",max_episode_steps=400)
register(id="ContinuousSlowRandom-v0", entry_point="driving.envs:GridworldContinuousSlowRandomInitEnv",max_episode_steps=400)
