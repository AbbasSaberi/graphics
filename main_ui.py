# # from nicegui import ui

# # with ui.scene1().classes('w-full h-64') as scene1:
# #     scene1.box1(1.8 , 1.8 , 5).material('black').move(x=-1.1, y=0, z= 2.5)
# #     scene1.box1(1.8 , 1.8 , 5).material('black').move(x=1.1, y=0, z= 2.5)
# #     scene1.box1(4 , 2 , 0.5).material('black').move(x=0, y=0, z=5.2)
# #     scene1.box1(4 , 2 , 0.4).material('black').move(x=0, y=0, z=5.6)
# #     scene1.box1(4 , 2 , 4).material('black').move(x=0, y=0, z=7.8)
# #     scene1.box1(0.2 , 2 , 0.2).material('black').move(x=0, y=-0.2, z=5.2)
# #     scene1.box1(1 , 1.4 , 3.5).material('black').move(x=-2.5,y=0,z=8.1)
# #     scene1.box1(1 , 1.4 , 3.5).material('black').move(x=2.5,y=0,z=8.1)
# #     scene1.box1(0.5 , 1.5 , 0.5).material('orange').move(x=-2.7,y=-0.1,z=6.4)
# #     scene1.box1(0.5 , 1.5 , 0.5).material('orange').move(x=2.7,y=-0.1,z=6.4)
# #     scene1.box1(4 , 2 , 3.5).material('black').move(x=0,y=0,z=11.5)
# #     scene1.box1(3 , 2 , 2.5).material('orange').move(x=0,y=-0.5,z=11.5)
# #     scene1.box1(0.8 , 2.5 , 1).material('white').move(x=0.8,y=-0.3,z=12)
# #     scene1.box1(0.8 , 2.5 , 1).material('white').move(x=-0.8,y=-0.3,z=12)
# #     scene1.box1(0.4 , 2.5 , 0.5).material('blue').move(x=-0.8,y=-0.4,z=12)
# #     scene1.box1(0.4 , 2.5 , 0.5).material('red').move(x=0.8,y=-0.4,z=12)
# #     scene1.box1(0.2 , 2.5 , 0.1).move(x=0.9,y=-0.4,z=12.2)
# #     scene1.box1(0.2 , 2.5 , 0.1).move(x=-0.7,y=-0.4,z=12.2)
# #     scene1.box1(3.5 , 2 , 1.5).material('black').move(x=0,y=-0.9,z=10.8)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('blue').move(x=-2.9,y=-0.6,z=7.4)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('blue').move(x=-2.9,y=0.6,z=8.4)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('blue').move(x=-2.9,y=-0.6,z=9.4)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('red').move(x=2.9,y=-0.6,z=7.4)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('red').move(x=2.9,y=0.6,z=8.4)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('red').move(x=2.9,y=-0.6,z=9.4)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('red').move(x=-1.9,y=-0.9,z=3.5)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('red').move(x=-1.9,y=0.9,z=4.5)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('red').move(x=-1.9,y=-0.9,z=5.5)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('blue').move(x=1.9,y=-0.9,z=3.5)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('blue').move(x=1.9,y=0.9,z=4.5)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('blue').move(x=1.9,y=-0.9,z=5.5)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('red').move(x=-0.8,y=-1,z=9)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('blue').move(x=-0.8,y=-1,z=8)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('blue').move(x=0.8,y=-1,z=9)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('red').move(x=0.8,y=-1,z=8)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('red').move(x=-0.8,y=1,z=9)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('blue').move(x=-0.8,y=1,z=8)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('blue').move(x=0.8,y=1,z=9)
# #     scene1.box1(0.3 , 0.3 , 0.3).material('red').move(x=0.8,y=1,z=8)
# #     scene1.sphere(150).material('yellow').move(x=600,y=-600,z=600)
# #     scene1.spot_light('yellow', intensity=1999, distance=10000, angle=10000000).move(600, -600, 600)

# # ui.run()
# # __--------------------------------------------------------------------------------------------------__
# # from nicegui import ui
# # from nicegui.events import KeyEventArguments
# # ui.label('''pleyer1(blue) \v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v
# # \v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v
# # \v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v
# # \v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v\v plyer2(red)''')

# # def handle_key(e: KeyEventArguments):
# #     # pleyer 1
# #     if e.modifiers and e.action.keydown:
# #         if e.key.arrow_left:
# #             box1.move(x=box1.x + -1, y=box1.y, z=box1.z)
# #             scene1.move_camera(x=box1.x + 2 , y=box1.y - 14 , z=box1.z + 14)
# #             box3.move(x=box3.x + -1, y=box3.y, z=box3.z)
# #         elif e.key.arrow_right:
# #             box1.move(x=box1.x + 1, y=box1.y, z=box1.z)
# #             scene1.move_camera(x=box1.x + 2 , y=box1.y - 14 , z=box1.z + 14)
# #             box3.move(x=box3.x + 1, y=box3.y, z=box3.z)
# #         elif e.key.arrow_up:
# #             box1.move(x=box1.x, y=box1.y + 1, z=box1.z)
# #             scene1.move_camera(x=box1.x + 2 , y=box1.y - 14 , z=box1.z + 14)
# #             box3.move(x=box3.x, y=box3.y + 1, z=box3.z)
# #         elif e.key.arrow_down:
# #             box1.move(x=box1.x, y=box1.y + -1, z=box1.z)
# #             scene1.move_camera(x=box1.x + 2 , y=box1.y - 14 , z=box1.z + 14)
# #             box3.move(x=box3.x, y=box3.y + -1, z=box3.z)
# #     # pleyer 2
# #         if e.key == 'a' or e.key == 'ش':
# #             box2.move(x=box2.x + -1, y=box2.y, z=box2.z)
# #             box4.move(x=box4.x + -1, y=box4.y, z=box4.z)
# #             scene2.move_camera(x=box4.x + -2 , y=box4.y - 14 , z=box4.z + 14)
# #         elif e.key == 'd' or e.key == 'ی':
# #             box2.move(x=box2.x + 1, y=box2.y, z=box2.z)
# #             box4.move(x=box4.x + 1, y=box4.y, z=box4.z)
# #             scene2.move_camera(x=box4.x + -2 , y=box4.y - 14 , z=box4.z + 14)
# #         elif e.key == 'w' or e.key == 'ص':
# #             box2.move(x=box2.x, y=box2.y + 1, z=box2.z)
# #             box4.move(x=box4.x, y=box4.y + 1, z=box4.z)
# #             scene2.move_camera(x=box4.x + -2 , y=box4.y - 14 , z=box4.z + 14)
# #         elif e.key == 's' or e.key == 'س':
# #             box2.move(x=box2.x, y=box2.y + -1, z=box2.z)
# #             box4.move(x=box4.x, y=box4.y + -1, z=box4.z)
# #             scene2.move_camera(x=box4.x + -2 , y=box4.y - 14 , z=box4.z + 14)
            

# # keyboard = ui.keyboard(on_key=handle_key)
# # with ui.scene().classes('w-full h-64') as scene1:
# #     scene1.cylinder().move(z=10000)
# # with ui.scene().classes('w-full h-64') as scene2:
# # # pleyer 1
# #     box1 = scene1.box().material('blue').move(x=1, y=-48, z=1)
# # # pleyer 2
# #     box2 = scene1.box().material('red').move(x=-1, y=-48, z=1)
# # # pleyer 1_3
# #     box3 = scene2.box().material('blue').move(x=1, y=-48, z=1)
# # # pleyer 2_4
# #     box4 = scene2.box().material('red').move(x=-1, y=-48, z=1)

# #     scene1.box(100 , 100 , 0.9).material('green')
# #     scene2.box(100 , 100 , 0.9).material('green')


# #     scene1.move_camera(x=box1.x + 2 , y=box1.y - 14 , z=box1.z + 14)
# #     scene2.move_camera(x=box4.x + -2 , y=box4.y - 14 , z=box4.z + 14)

# # #camera
# #     camera1 = scene1.box(0.2 , 0.2 , 2).material('black').move(x=8 , y=-42 , z=1)
# #     scene1.box(0.5 , 0.5 , 0.5).material('silver').move(x=8 , y=-42 , z=2)
# #     scene1.box(0.3 , 0.3 , 0.3).material('silver').move(x=7.65 , y=-42 , z=2)
# #     scene1.box(0.1 , 0.3 , 0.3).material('withe').move(x=7.45 , y=-42 , z=2)

# #     camera2 = scene1.box(0.2 , 0.2 , 0.2).material

# #     scene1.box(2.8 , 0.2 , 1).material('yellow').move(x=0 , y=-46.5 , z=0.1)
# #     scene2.box(2.8 , 0.2 , 1).material('yellow').move(x=0 , y=-46.5 , z=0.1)

# #     scene1.box(3 , 8 , 1).material('gray').move(x=0 , y=-45)
# #     scene2.box(3 , 8 , 1).material('gray').move(x=0 , y=-45)

# #     scene1.box(5 , 3 , 1).material('gray').move(x=4 , y=-42.5)
# #     scene2.box(5 , 3 , 1).material('gray').move(x=4 , y=-42.5)
    
# #     scene1.box(3 , 5 , 1).material('gray').move(x=5 , y=-40.5)
# #     scene2.box(3 , 5 , 1).material('gray').move(x=5 , y=-40.5)
    
# #     scene1.box(4 , 3 , 1).material('gray').move(x=8 , y=-39.5)
# #     scene2.box(4 , 3 , 1).material('gray').move(x=8 , y=-39.5)
    
# #     scene1.box(3 , 6 , 1).material('gray').move(x=11 , y=-38)
# #     scene2.box(3 , 6 , 1).material('gray').move(x=11 , y=-38)
    
# #     scene1.box(20 , 3 , 1).material('gray').move(x=2.5 , y=-34)
# #     scene2.box(20 , 3 , 1).material('gray').move(x=2.5 , y=-34)
    
# #     scene1.box(3 , 14 , 1).material('gray').move(x=-6 , y=-42)
# #     scene2.box(3 , 14 , 1).material('gray').move(x=-6 , y=-42)
    
# #     scene1.box(6 , 3 , 1).material('gray').move(x=-10 , y=-47.5)
# #     scene2.box(6 , 3 , 1).material('gray').move(x=-10 , y=-47.5)
    
# #     scene1.box(3 , 8 , 1).material('gray').move(x=-11.5 , y=-43)
# #     scene2.box(3 , 8 , 1).material('gray').move(x=-11.5 , y=-43)
    
# #     scene1.box(5 , 3 , 1).material('gray').move(x=-14 , y=-40.5)
# #     scene2.box(5 , 3 , 1).material('gray').move(x=-14 , y=-40.5)
    
# #     scene1.box(3 , 5 , 1).material('gray').move(x=-18 , y=-39.5)
# #     scene2.box(3 , 5 , 1).material('gray').move(x=-18 , y=-39.5)
    
# #     scene1.box(8 , 3 , 1).material('gray').move(x=-20.5 , y=-36.5)
# #     scene2.box(8 , 3 , 1).material('gray').move(x=-20.5 , y=-36.5)
    
# #     scene1.box(3 , 14 , 1).material('gray').move(x=-23 , y=-42)
# #     scene2.box(3 , 14 , 1).material('gray').move(x=-23 , y=-42)
    
# #     scene1.box(10 , 3 , 1).material('gray').move(x=-26.5 , y=-47.5)
# #     scene2.box(10 , 3 , 1).material('gray').move(x=-26.5 , y=-47.5)
    
# #     scene1.box(3 , 18 , 1).material('gray').move(x=-30 , y=-38)
# #     scene2.box(3 , 18 , 1).material('gray').move(x=-30 , y=-38)
    
# #     scene1.box(14 , 3 , 1).material('gray').move(x=-24 , y=-30.5)
# #     scene2.box(14 , 3 , 1).material('gray').move(x=-24 , y=-30.5)
    
# #     scene1.box(3 , 5 , 1).material('gray').move(x=-18.5 , y=-28)
# #     scene2.box(3 , 5 , 1).material('gray').move(x=-18.5 , y=-28)
    
# #     scene1.box(45 , 3 , 1).material('gray').move(x=5.5 , y=-27)
# #     scene2.box(45 , 3 , 1).material('gray').move(x=5.5 , y=-27)
    
# #     scene1.box(3 , 8 , 1).material('gray').move(x=26.5 , y=-31)
# #     scene2.box(3 , 8 , 1).material('gray').move(x=26.5 , y=-31)
    
# #     scene1.box(8 , 3 , 1).material('gray').move(x=21 , y=-33.5)
# #     scene2.box(8 , 3 , 1).material('gray').move(x=21 , y=-33.5)
# # ui.run()
# __----------------------------------------------------------------------------------------------------------__
# from nicegui import ui

# with ui.scene().classes('w-full h-64') as scene:
#     scene.move_camera(-2 ,10 , 5)
#     scene.box(100 , 50 , 1.5).material('gray')
#     for line in range(5):
#         scene.box(6 , 1.5 , 1.51).move(x=-line * 10)
#     for line in range(5):
#         scene.box(6 , 1.5 , 1.51).move(x= line * 10)
# # Pleyer
#     scene.box(0.5 , 1 , 1.5).material('blue').move(z=1.5)
#     scene.box(0.5 , 1.25 , 1.5).material('cyan').move(z=3)
#     scene.box(0.49 , 3 , 0.5).material('beige').move(z=3.4)
#     scene.box(1 , 1 , 1).material('beige').move(z=4.2)
#     scene.box(1 , 1.3 , 1.2).material('black').move(x=0.01 , z=4.3)



# #    scene.text('\vGAIME-OVER\v')

# ui.run()
# __----------------------------------------------------------------------------------------------------------__
from enum import Enum

a = int(input('The sides of the playground : '))
G1 = input('Gate point 1 : ').split(',')
G2 = input('Gate point 2 : ').split(',')
b = input('ball point : ').split(',')
c = input('Robot player point : ').split(',')

from nicegui import ui
from nicegui.elements.html import Html
from nicegui.elements.timer import Timer

Direction = Enum('Direction', ['Up', 'Down', 'Right', 'Left'])

class Position():
    def __init__ (self, x, y):
        self.x = x
        self.y = y

class State():
    def __init__(self):
        self.iteration = 0
        self.robot_pos = Position(0, 0)
        self.ball_pos = Position(0, 0)
        self.grid_size = 0
        self.cell_size = 0
        self.solution_path = ''
        self.start_pos = Position(0, 0)
        self.gate = (Position(0,0), Position(0, 0))
        self.ball_color = 'black'
        self.robot_color = 'black'
        self.path_color = 'black'
        self.gate_color = 'black'

def build_svg( state: State) -> str:
    cell_size = state.cell_size
    grid_size = state.grid_size

    width = cell_size * grid_size + 1
    height = cell_size * grid_size + 1

    current_path = state.solution_path.split(' ')[0:state.iteration]

    # draw solution path
    path = draw_path(state.start_pos.x, state.start_pos.y, current_path, grid_size, cell_size, state.path_color)

    # draw gate
    if(state.gate[0].x == state.gate[1].x):
        gate_start_x = state.gate[0].x
        gate_start_y = min(state.gate[0].y, state.gate[1].y)
        gate_path = 'U' * abs(state.gate[0].y - state.gate[1].y)
    else:
        gate_start_x = min(state.gate[0].x, state.gate[1].x)
        gate_start_y = state.gate[0].y
        gate_path = 'R' * abs(state.gate[0].x - state.gate[1].x)

    gate = draw_path(gate_start_x, gate_start_y, gate_path, grid_size, cell_size, state.gate_color)

    # draw ball
    ball_x = get_x_position(state.ball_pos.x, grid_size, cell_size)
    ball_y = get_y_position(state.ball_pos.y, grid_size, cell_size)
    ball = f'<circle cx="{ball_x}" cy="{ball_y}" r="10" fill="{state.ball_color}" />'

    last_movement = state.solution_path.split(' ')[state.iteration]
    last_movement_direction = get_direction(last_movement)

    # draw robot
    robot_pos_x = get_x_position(state.robot_pos.x, grid_size, cell_size)
    robot_pos_y = get_y_position(state.robot_pos.y, grid_size, cell_size)
    robot = f'<circle cx="{robot_pos_x}" cy="{robot_pos_y}" r="20" fill="{state.robot_color}" />'

    robot_next_pos = calculate_next_position(state.robot_pos, last_movement_direction)
    state.robot_pos = robot_next_pos # update robot position

    if(state.robot_pos.x == state.ball_pos.x and state.robot_pos.y == state.ball_pos.y):
        ball_next_pos = calculate_next_position(state.ball_pos, last_movement_direction)
        state.ball_pos = ball_next_pos
    
    # draw game board
    return f'''
        <svg id='patternId' width='{width}' height='{height}' xmlns='http://www.w3.org/2000/svg'>
        <defs><pattern id='a' patternUnits='userSpaceOnUse' width='{cell_size}' height='{cell_size}' patternTransform='rotate(0)'>
        <rect x='0' y='0' width='100%' height='100%' fill='hsla(0,0%,100%,1)'/>
        <path d='M 0,0 V {cell_size} Z M 0,0 H {cell_size} Z'  stroke-width='1' stroke='hsla(133, 35%, 32%, 1)' fill='none'/>
        </pattern></defs>
        <rect width='100%' height='100%'  fill='url(#a)'/>
        
        {path}
        {gate}
        {ball}
        {robot}
        
        </svg>
    '''

def get_x_position(pos, grid_size, cell_size):
    return pos * cell_size

def get_y_position(pos, grid_size, cell_size):
    return (grid_size - pos) * cell_size

def draw_path(x, y, path, grid_size, cell_size, color):
    lines = []

    next_x = x
    next_y = y

    for dir in path:
        direction: Direction = get_direction(dir)
        lines.append(generate_line(next_x, next_y, direction, 1, grid_size, cell_size, color))
        next_x, next_y = calculate_next_position_xy(next_x, next_y, direction)

    return str.join(" ", lines)

def calculate_next_position(pos: Position, direction: Direction):
    (next_x, next_y) = calculate_next_position_xy(pos.x, pos.y, direction)
    return Position(next_x, next_y)

def calculate_next_position_xy(x, y, direction: Direction):
    match direction:
        case Direction.Down:
            return (x, y - 1)
        case Direction.Up:
            return (x, y + 1)
        case Direction.Left:
            return (x - 1, y)
        case Direction.Right:
            return (x + 1, y)

def get_direction(dir):
    match dir:
        case 'D':
            return Direction.Down
        case 'U':
            return Direction.Up
        case 'L':
            return Direction.Left
        case 'R':
            return Direction.Right

def generate_line(x, y, direction: Direction, length, grid_size, cell_size, color):
    target_x = x
    target_y = (grid_size) - y

    match direction:
        case Direction.Down:
            target_y = target_y + length # SVG grid is top to bottom
        case Direction.Up:
            target_y = target_y - length # SVG grid is top to bottom
        case Direction.Right:
            target_x = target_x + length
        case Direction.Left:
            target_x = target_x - length

    scaled_x = x * cell_size
    scaled_y = ((grid_size) - y) * cell_size

    scaled_target_x = target_x * cell_size
    scaled_target_y = target_y * cell_size
    return f'''
    <path d='M {scaled_x} {scaled_y} L {scaled_target_x} {scaled_target_y}'  stroke-width='3' stroke='{color}'/>
    '''

def next_frame(body: Html, state: State):
    body.set_content(build_svg(state))
    state.iteration = state.iteration + 1

def toggle_timer(timer: Timer):
    if(timer.active):
        timer.deactivate()
    else:
        timer.activate()

def reset(state: State):
    state.ball_pos = Position(2, 1)
    state.robot_pos = Position(7, 4)
    state.grid_size = 10
    state.cell_size = 50
    state.iteration = 0
    state.solution_path = 'D D D D L L L L L U U U U U U L U R R R R R R R R R'
    state.start_pos = state.robot_pos
    state.gate = (Position(10, 5), Position(10, 8))
    state.ball_color = 'red'
    state.robot_color = 'green'
    state.path_color = 'orange'
    state.gate_color = 'blue'

interval = 1.0 # seconds
timer = ui.timer(interval, lambda: next_frame(body, state))
timer.deactivate()

state = State()

with ui.row():
    ui.button('Play / Pause', on_click= lambda: toggle_timer(timer))
    ui.button('Reset', on_click= lambda: reset(state))

body = ui.html().classes('self-center')

reset(state)

ui.run()