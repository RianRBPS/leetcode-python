class Solution(object):
    def queryResults(self, limit, queries):
        """
        given a set of ball numbered from 0 to limit
        initially all bals are uncolored
        each query assigns a color y to a ball x
        if a ball was previosly colored, it replaces its color with a new one
        we track how many unique colors exist after each query
        the result is a list of unique color counts at each step
        """
        ball_colors = {}
        color_count = {}
        result = []

        for ball, color in queries:
            if ball in ball_colors:
                old_color = ball_colors[ball]
                # decrease count of the old color
                color_count[old_color] -= 1
                # if no ball has this color anymore, remove it from the count
                if color_count[old_color] == 0:
                    del color_count[old_color]
            # assigns new color to the ball
            ball_colors[ball] = color
            # adds new color to the set of distinct colors
            color_count[color] = color_count.get(color, 0) + 1
            # append the count of distinct colors after each query
            result.append(len(color_count))

        return result
        
