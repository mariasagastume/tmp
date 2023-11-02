from exp import ex


def run():
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (4, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_1',
        'comment': 'bump_centers: (0, 0, 3), (4, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (5, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_2',
        'comment': 'bump_centers: (0, 0, 3), (5, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (6, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_3',
        'comment': 'bump_centers: (0, 0, 3), (6, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (5, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_4',
        'comment': 'bump_centers: (0, 0, 3), (5, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (6, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_5',
        'comment': 'bump_centers: (0, 0, 3), (6, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (7, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_6',
        'comment': 'bump_centers: (0, 0, 3), (7, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (8, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_7',
        'comment': 'bump_centers: (0, 0, 3), (8, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (9, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_8',
        'comment': 'bump_centers: (0, 0, 3), (9, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (10, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_9',
        'comment': 'bump_centers: (0, 0, 3), (10, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (9, 6, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_10',
        'comment': 'bump_centers: (0, 0, 3), (9, 6, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (8, 8, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_11',
        'comment': 'bump_centers: (0, 0, 3), (8, 8, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (10, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_12',
        'comment': 'bump_centers: (0, 0, 3), (10, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (9, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_13',
        'comment': 'bump_centers: (0, 0, 3), (9, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (10, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_14',
        'comment': 'bump_centers: (0, 0, 3), (10, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (11, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_15',
        'comment': 'bump_centers: (0, 0, 3), (11, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (7, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_16',
        'comment': 'bump_centers: (0, 0, 3), (7, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (8, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_17',
        'comment': 'bump_centers: (0, 0, 3), (8, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (9, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_18',
        'comment': 'bump_centers: (0, 0, 3), (9, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 3.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (10, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 3.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_straight_2_bumps_19',
        'comment': 'bump_centers: (0, 0, 3), (10, 0, 3)'})




    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (4, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_1',
        'comment': 'bump_centers: (0, 0, 3), (4, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (5, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_2',
        'comment': 'bump_centers: (0, 0, 3), (5, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (6, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_3',
        'comment': 'bump_centers: (0, 0, 3), (6, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (5, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_4',
        'comment': 'bump_centers: (0, 0, 3), (5, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (6, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_5',
        'comment': 'bump_centers: (0, 0, 3), (6, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (7, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_6',
        'comment': 'bump_centers: (0, 0, 3), (7, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (8, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_7',
        'comment': 'bump_centers: (0, 0, 3), (8, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (9, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_8',
        'comment': 'bump_centers: (0, 0, 3), (9, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (10, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_9',
        'comment': 'bump_centers: (0, 0, 3), (10, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (9, 6, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_10',
        'comment': 'bump_centers: (0, 0, 3), (9, 6, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (8, 8, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_11',
        'comment': 'bump_centers: (0, 0, 3), (8, 8, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (10, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_12',
        'comment': 'bump_centers: (0, 0, 3), (10, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (9, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_13',
        'comment': 'bump_centers: (0, 0, 3), (9, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (10, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_14',
        'comment': 'bump_centers: (0, 0, 3), (10, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (11, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_15',
        'comment': 'bump_centers: (0, 0, 3), (11, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (7, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_16',
        'comment': 'bump_centers: (0, 0, 3), (7, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (8, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_17',
        'comment': 'bump_centers: (0, 0, 3), (8, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (9, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_18',
        'comment': 'bump_centers: (0, 0, 3), (9, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 3), (10, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_3_19',
        'comment': 'bump_centers: (0, 0, 3), (10, 0, 3)'})




    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (4, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_1',
        'comment': 'bump_centers: (0, 0, 2), (4, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (5, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_2',
        'comment': 'bump_centers: (0, 0, 2), (5, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (6, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_3',
        'comment': 'bump_centers: (0, 0, 2), (6, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (5, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_4',
        'comment': 'bump_centers: (0, 0, 2), (5, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (6, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_5',
        'comment': 'bump_centers: (0, 0, 2), (6, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (7, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_6',
        'comment': 'bump_centers: (0, 0, 2), (7, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (8, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_7',
        'comment': 'bump_centers: (0, 0, 2), (8, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (9, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_8',
        'comment': 'bump_centers: (0, 0, 2), (9, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (10, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_9',
        'comment': 'bump_centers: (0, 0, 2), (10, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (9, 6, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_10',
        'comment': 'bump_centers: (0, 0, 2), (9, 6, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (8, 8, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_11',
        'comment': 'bump_centers: (0, 0, 2), (8, 8, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (10, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_12',
        'comment': 'bump_centers: (0, 0, 2), (10, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (9, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_13',
        'comment': 'bump_centers: (0, 0, 2), (9, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (10, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_14',
        'comment': 'bump_centers: (0, 0, 2), (10, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (11, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_15',
        'comment': 'bump_centers: (0, 0, 2), (11, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (7, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_16',
        'comment': 'bump_centers: (0, 0, 2), (7, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (8, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_17',
        'comment': 'bump_centers: (0, 0, 2), (8, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (9, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_18',
        'comment': 'bump_centers: (0, 0, 2), (9, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 2), (10, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_2_19',
        'comment': 'bump_centers: (0, 0, 2), (10, 0, 3)'})




    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (4, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_1',
        'comment': 'bump_centers: (0, 0, 1), (4, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (5, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_2',
        'comment': 'bump_centers: (0, 0, 1), (5, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (6, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_3',
        'comment': 'bump_centers: (0, 0, 1), (6, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (5, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_4',
        'comment': 'bump_centers: (0, 0, 1), (5, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (6, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_5',
        'comment': 'bump_centers: (0, 0, 1), (6, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (7, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_6',
        'comment': 'bump_centers: (0, 0, 1), (7, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (8, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_7',
        'comment': 'bump_centers: (0, 0, 1), (8, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (9, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_8',
        'comment': 'bump_centers: (0, 0, 1), (9, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (10, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_9',
        'comment': 'bump_centers: (0, 0, 1), (10, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (9, 6, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_10',
        'comment': 'bump_centers: (0, 0, 1), (9, 6, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (8, 8, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_11',
        'comment': 'bump_centers: (0, 0, 1), (8, 8, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (10, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_12',
        'comment': 'bump_centers: (0, 0, 1), (10, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (9, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_13',
        'comment': 'bump_centers: (0, 0, 1), (9, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (10, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_14',
        'comment': 'bump_centers: (0, 0, 1), (10, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (11, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_15',
        'comment': 'bump_centers: (0, 0, 1), (11, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (7, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_16',
        'comment': 'bump_centers: (0, 0, 1), (7, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (8, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_17',
        'comment': 'bump_centers: (0, 0, 1), (8, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (9, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_18',
        'comment': 'bump_centers: (0, 0, 1), (9, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 1), (10, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_1_19',
        'comment': 'bump_centers: (0, 0, 1), (10, 0, 3)'})




    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (4, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_1',
        'comment': 'bump_centers: (0, 0, 0), (4, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (5, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_2',
        'comment': 'bump_centers: (0, 0, 0), (5, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (6, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_3',
        'comment': 'bump_centers: (0, 0, 0), (6, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (5, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_4',
        'comment': 'bump_centers: (0, 0, 0), (5, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (6, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_5',
        'comment': 'bump_centers: (0, 0, 0), (6, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (7, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_6',
        'comment': 'bump_centers: (0, 0, 0), (7, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (8, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_7',
        'comment': 'bump_centers: (0, 0, 0), (8, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (9, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_8',
        'comment': 'bump_centers: (0, 0, 0), (9, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (10, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_9',
        'comment': 'bump_centers: (0, 0, 0), (10, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (9, 6, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_10',
        'comment': 'bump_centers: (0, 0, 0), (9, 6, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (8, 8, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_11',
        'comment': 'bump_centers: (0, 0, 0), (8, 8, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (10, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_12',
        'comment': 'bump_centers: (0, 0, 0), (10, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (9, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_13',
        'comment': 'bump_centers: (0, 0, 0), (9, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (10, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_14',
        'comment': 'bump_centers: (0, 0, 0), (10, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (11, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_15',
        'comment': 'bump_centers: (0, 0, 0), (11, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (7, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_16',
        'comment': 'bump_centers: (0, 0, 0), (7, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (8, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_17',
        'comment': 'bump_centers: (0, 0, 0), (8, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (9, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_18',
        'comment': 'bump_centers: (0, 0, 0), (9, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 0), (10, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_0_19',
        'comment': 'bump_centers: (0, 0, 0), (10, 0, 3)'})




    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (4, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_1',
        'comment': 'bump_centers: (0, 0, 4), (4, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (5, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_2',
        'comment': 'bump_centers: (0, 0, 4), (5, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (6, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_3',
        'comment': 'bump_centers: (0, 0, 4), (6, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (5, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_4',
        'comment': 'bump_centers: (0, 0, 4), (5, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (6, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_5',
        'comment': 'bump_centers: (0, 0, 4), (6, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (7, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_6',
        'comment': 'bump_centers: (0, 0, 4), (7, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (8, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_7',
        'comment': 'bump_centers: (0, 0, 4), (8, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (9, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_8',
        'comment': 'bump_centers: (0, 0, 4), (9, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (10, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_9',
        'comment': 'bump_centers: (0, 0, 4), (10, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (9, 6, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_10',
        'comment': 'bump_centers: (0, 0, 4), (9, 6, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (8, 8, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_11',
        'comment': 'bump_centers: (0, 0, 4), (8, 8, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (10, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_12',
        'comment': 'bump_centers: (0, 0, 4), (10, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (9, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_13',
        'comment': 'bump_centers: (0, 0, 4), (9, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (10, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_14',
        'comment': 'bump_centers: (0, 0, 4), (10, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (11, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_15',
        'comment': 'bump_centers: (0, 0, 4), (11, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (7, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_16',
        'comment': 'bump_centers: (0, 0, 4), (7, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (8, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_17',
        'comment': 'bump_centers: (0, 0, 4), (8, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (9, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_18',
        'comment': 'bump_centers: (0, 0, 4), (9, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 4), (10, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_4_19',
        'comment': 'bump_centers: (0, 0, 4), (10, 0, 3)'})




    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (4, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_1',
        'comment': 'bump_centers: (0, 0, 5), (4, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (5, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_2',
        'comment': 'bump_centers: (0, 0, 5), (5, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (6, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_3',
        'comment': 'bump_centers: (0, 0, 5), (6, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (5, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_4',
        'comment': 'bump_centers: (0, 0, 5), (5, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (6, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_5',
        'comment': 'bump_centers: (0, 0, 5), (6, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (7, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_6',
        'comment': 'bump_centers: (0, 0, 5), (7, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (8, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_7',
        'comment': 'bump_centers: (0, 0, 5), (8, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (9, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_8',
        'comment': 'bump_centers: (0, 0, 5), (9, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (10, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_9',
        'comment': 'bump_centers: (0, 0, 5), (10, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (9, 6, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_10',
        'comment': 'bump_centers: (0, 0, 5), (9, 6, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (8, 8, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_11',
        'comment': 'bump_centers: (0, 0, 5), (8, 8, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (10, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_12',
        'comment': 'bump_centers: (0, 0, 5), (10, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (9, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_13',
        'comment': 'bump_centers: (0, 0, 5), (9, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (10, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_14',
        'comment': 'bump_centers: (0, 0, 5), (10, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (11, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_15',
        'comment': 'bump_centers: (0, 0, 5), (11, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (7, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_16',
        'comment': 'bump_centers: (0, 0, 5), (7, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (8, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_17',
        'comment': 'bump_centers: (0, 0, 5), (8, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (9, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_18',
        'comment': 'bump_centers: (0, 0, 5), (9, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 5), (10, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_5_19',
        'comment': 'bump_centers: (0, 0, 5), (10, 0, 3)'})




    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (4, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_1',
        'comment': 'bump_centers: (0, 0, 6), (4, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (5, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_2',
        'comment': 'bump_centers: (0, 0, 6), (5, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (6, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_3',
        'comment': 'bump_centers: (0, 0, 6), (6, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (5, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_4',
        'comment': 'bump_centers: (0, 0, 6), (5, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (6, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_5',
        'comment': 'bump_centers: (0, 0, 6), (6, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (7, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_6',
        'comment': 'bump_centers: (0, 0, 6), (7, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (8, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_7',
        'comment': 'bump_centers: (0, 0, 6), (8, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (9, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_8',
        'comment': 'bump_centers: (0, 0, 6), (9, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (10, 4, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_9',
        'comment': 'bump_centers: (0, 0, 6), (10, 4, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (9, 6, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_10',
        'comment': 'bump_centers: (0, 0, 6), (9, 6, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (8, 8, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_11',
        'comment': 'bump_centers: (0, 0, 6), (8, 8, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (10, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_12',
        'comment': 'bump_centers: (0, 0, 6), (10, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (9, 3, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_13',
        'comment': 'bump_centers: (0, 0, 6), (9, 3, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (10, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_14',
        'comment': 'bump_centers: (0, 0, 6), (10, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (11, 2, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_15',
        'comment': 'bump_centers: (0, 0, 6), (11, 2, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (7, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_16',
        'comment': 'bump_centers: (0, 0, 6), (7, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (8, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_17',
        'comment': 'bump_centers: (0, 0, 6), (8, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (9, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_18',
        'comment': 'bump_centers: (0, 0, 6), (9, 0, 3)'})
    ex.run(config_updates={
        'tau': 0.1,
        'simulation_duration': 10.7,
        'input': [{
            'duration': 0.2,
            'cmds': [{'cmd': 'input_freq',
                      'bump_centers': [(0, 0, 6), (10, 0, 3)]}]
        }, {
            'duration': 0.5,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 1,
                      'pos_rot_shift_inhib': 1,
                      'neg_rot_shift_inhib': 1}]
        }, {
            'duration': 10.0,
            'cmds': [{'cmd': 'manual',
                      'shift_inhib': 0.02,
                      'pos_rot_shift_inhib': 0.02,
                      'neg_rot_shift_inhib': 1}]
        }],
        'use_loihi': True,
        'textid': 'multi_bump_interference_circular_2_bumps_6_19',
        'comment': 'bump_centers: (0, 0, 6), (10, 0, 3)'})
    # ex.run(config_updates={
    #     'tau': 0.1,
    #     'simulation_duration': 11.9,
    #     'input': [{
    #         'duration': 0.2,
    #         'cmds': [{'cmd': 'input_freq',
    #                   'bump_centers': [(8, 8, 3)]}]
    #     }, {
    #         'duration': 0.5,
    #         'cmds': [{'cmd': 'manual',
    #                   'shift_inhib': 1,
    #                   'pos_rot_shift_inhib': 1,
    #                   'neg_rot_shift_inhib': 1}]
    #     }, {
    #         'duration': 1.55,
    #         'cmds': [{'cmd': 'manual',
    #                   'shift_inhib': 0.01,
    #                   'pos_rot_shift_inhib': 0.01,
    #                   'neg_rot_shift_inhib': 1}]
    #     }, {
    #         'duration': 2.5,
    #         'cmds': [{'cmd': 'manual',
    #                   'shift_inhib': 0.01,
    #                   'pos_rot_shift_inhib': 1,
    #                   'neg_rot_shift_inhib': 1}]
    #     }, {
    #         'duration': 3.1,
    #         'cmds': [{'cmd': 'manual',
    #                   'shift_inhib': 0.01,
    #                   'pos_rot_shift_inhib': 1,
    #                   'neg_rot_shift_inhib': 0.01}]
    #     }, {
    #         'duration': 2.5,
    #         'cmds': [{'cmd': 'manual',
    #                   'shift_inhib': 0.01,
    #                   'pos_rot_shift_inhib': 1,
    #                   'neg_rot_shift_inhib': 1}]
    #     }, {
    #         'duration': 1.55,
    #         'cmds': [{'cmd': 'manual',
    #                   'shift_inhib': 0.01,
    #                   'pos_rot_shift_inhib': 0.01,
    #                   'neg_rot_shift_inhib': 1}]
    #     }],
    #     'use_loihi': True,
    #     'comment': 'loihi; tau=0.1; default synapse on input-related connections and from attractor_ens to shift/rot_ens',
    #     'enable_status_mails': True})


if __name__ == '__main__':
    run()
