""" Module containing methods related to map creation/import/conversion """

from .screen import Screen
from .graphics import Color

class Map:
    """ Everything regarding the game map """

    @staticmethod
    def draw_map(level, char_img):
        """ Map rendering from imported file """
        column_to_draw = []
        map_to_draw = []
        Screen.DISPLAYSURF.fill(Color.WHITE) # This is to avoid overlapping of tiles
        max_x = Screen.MAXXTILE
        max_y = Screen.MAXYTILE
        extra_space = Screen.EXTRATILES

        rendered_array_width = range(int(level.player_coords[0])-int((max_x/2)), int(level.player_coords[0])+int((max_x//2))+extra_space)
        rendered_array_height = range(int(level.player_coords[1])-int((max_y/2)), int(level.player_coords[1])+int((max_y//2))+extra_space)
        # using as center player coordinates (since player is always drawn in the center) we draw only data from the array
        for i in rendered_array_width:
            for j in rendered_array_height:
                # up to max_x or max_y. If we have any index values that goes negative or over the limit, we print background
                if i < 0 or j < 0 or i > level.dimension[1]-1 or j > level.dimension[0]-1:
                    column_to_draw.append(level.tile_background) # Out of map bound
                else:
                    column_to_draw.append(level.tile_map[i][j])
            map_to_draw.append(column_to_draw)
            column_to_draw = []
        row = 0
        column = 0

        for line in map_to_draw:
            for tile in line:
                Screen.DISPLAYSURF.blit(tile, (row, column))
                column += Screen.TILESIDE
            row += Screen.TILESIDE
            column = 0

        # the player is always drawn in the center of the screen (PLAYERXONSCREEN, PLAYERYONSCREEN)
        # we do this at the end to overwrite the floor in player's place
        Screen.DISPLAYSURF.blit(char_img, (Screen.PLAYERXONSCREEN, Screen.PLAYERYONSCREEN))

        # to print npc in the correct place we convert the coords they have in the array with the screen coordinates
        # (screen is always a subset of the map).
        for npc in level.npc_array:
            if npc.x_coord in rendered_array_width and npc.y_coord in rendered_array_height:
                render_coordinate = Map.arr_coord_to_render_coord(npc.x_coord, npc.y_coord, rendered_array_width, rendered_array_height)
                Screen.DISPLAYSURF.blit(npc.current_tile, (render_coordinate[0] * Screen.TILESIDE, render_coordinate[1] * Screen.TILESIDE))

    @staticmethod
    def arr_coord_to_render_coord(npc_x, npc_y, rendered_array_width, rendered_array_height):
        """Converting map array coordinates to actual rendering coordinate"""
        x_rendered = 0
        y_rendered = 0
        for idx, i in enumerate(rendered_array_width):
            if i == npc_x:
                x_rendered = idx
        for idx, j in enumerate(rendered_array_height):
            if j == npc_y:
                y_rendered = idx

        return [x_rendered, y_rendered]
