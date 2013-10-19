# This file is part of Irianas (Client).
# Copyright (C) 2013 Irisel Gonzalez.
# Authors: Irisel Gonzalez <irisel.gonzalez@gmail.com>
#
import psutil


class MonitorSystem(object):

    def get_memory_used(self, percent=False):
        mem = psutil.virtual_memory()
        if percent:
            return mem[2]
        else:
            return mem[0] * (mem[2] / 100)

    def get_memory_free(self, percent=False):
        mem = psutil.virtual_memory()
        if percent:
            return 100 - mem[2]
        else:
            return mem[1]

    def get_cpu_porcent(self, interval=5):
        return psutil.cpu_percent(interval=interval)

    def get_disk_used(self, percent=False):
        disks = psutil.disk_partitions()
        total = 0
        for disk in disks:
            usage = psutil.disk_usage(disk[1])
            if percent:
                total += usage[3]
            else:
                total += usage[0] * (usage[3] / 100)
        if percent:
            total /= len(disks)
        return total
