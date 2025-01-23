from block import Block
from item import Item

class Stage():
    blocks_shape = (27, 18)

    def __init__(self, blocks, start_point):
        self.blocks = blocks
        self.start_point = start_point

    def pos_converter(pos: tuple[int, int]):
        return (pos[0] * 40, pos[1] * 40)
    
    def from_stage_file(file: str, start_point: tuple[int, int]):
        blocks = []
        with open(file, 'r') as f:
            while True:
                line = f.readline()
                if not line: break
                line = list(line)
                line.pop()
                blocks.append(line)
        
        return Stage(blocks, start_point)
    
    def get_game_blocks(self):
        result = []
        for y in range(self.blocks_shape[1]-1):
            for x in range(self.blocks_shape[0]):
                if self.blocks[y][x] != '0' and self.blocks[y][x].isdecimal():
                    result.append(Block(int(self.blocks[y][x]), 
                                        Stage.pos_converter((x,y))
                                        ))
        return result
    
    def get_game_items(self):
        result = []
        for y in range(self.blocks_shape[1]-1):
            for x in range(self.blocks_shape[0]):
                if not self.blocks[y][x].isdecimal():
                    result.append(Item(self.blocks[y][x], 
                                        Stage.pos_converter((x,y))
                                        ))
        # for y in range(self.blocks_shape[1]-1):
        #     for x in range(self.blocks_shape[0]):
        #         if self.blocks[y][x] != 0:
        #             result.append(Block(self.blocks[y][x], 
        #                                 self.pos_converter((x,y))
        #                                 ).to_string())
        return result