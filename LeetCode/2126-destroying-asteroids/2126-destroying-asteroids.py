class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        n = len(asteroids)
        asteroids.sort()
        for i in range(n):
            if mass >= asteroids[i]:
                mass += asteroids[i]
            else:
                return False

        return True