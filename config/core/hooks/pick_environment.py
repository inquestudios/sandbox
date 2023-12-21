# Copyright (c) 2018 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Hook which chooses an environment file to use based on the current context.
"""

from tank import Hook
import sgtk


class PickEnvironment(Hook):
    def execute(self, context, **kwargs):
        """
        The default implementation assumes there are three environments, called shot, asset
        and project, and switches to these based on entity type.
        """

        # Get the engine instance that is currently running.
        current_engine = sgtk.platform.current_engine()

        if context.source_entity:
            if context.source_entity["type"] == "Version":
                return "version"
            elif context.source_entity["type"] == "PublishedFile":
                return "publishedfile"
            elif context.source_entity["type"] == "Playlist":
                return "playlist"
            elif context.source_entity["type"] == "CustomEntity01":
                return "material"
            elif context.source_entity["type"] == "CustomEntity02":
                return "scene"              

        if context.project is None:
            # Our context is completely empty. We're going into the site context.
            return "site"

        if context.entity is None:
            # We have a project but not an entity.
            return "project"

        if context.entity and context.step is None:
            # We have an entity but no step.
            sg = current_engine.shotgun
            sg_shot=sg.find_one("Shot", [["id", "is", context.entity["id"]]], ["sg_shot_type"])
            shot_type=sg_shot["sg_shot_type"]

            if context.entity["type"] == "Shot"  and not (shot_type == "showroom"):
                return "shot"
            if context.entity["type"] == "Shot" and shot_type == "showroom":
                return "showroom"
            if context.entity["type"] == "Asset":
                return "asset"
            if context.entity["type"] == "Sequence":
                return "sequence"
            if context.entity["type"] == "Episode":
                return "episode" 
            if context.entity["type"] == "CustomEntity01": 
                return "material"
            if context.entity["type"] == "CustomEntity02": 
                return "scene"

        if context.entity and context.step:
            # We have a step and an entity.
            sg = current_engine.shotgun
            sg_shot=sg.find_one("Shot", [["id", "is", context.entity["id"]]], ["sg_shot_type"])
            shot_type=sg_shot["sg_shot_type"]
            
            if context.entity["type"] == "Shot" and context.step["name"] == "DFT":
                return "shot_step_render"
            if context.entity["type"] == "Shot" and context.step["name"] == "RND":
                return "shot_step_render"
            if context.entity["type"] == "Shot" and context.step["name"] == "PST":
                return "shot_step_post"
            if context.entity["type"] == "Shot" and not (shot_type == "showroom"):
                return "shot_step"
            if context.entity["type"] == "Shot" and shot_type == "showroom" and not(context.step["name"] == "AR", "DFT", "RND", "SPR"):
                return "showroom_step_post"
            if context.entity["type"] == "Shot" and shot_type == "showroom" and context.step["name"] == "AR":
                return "showroom_step_ar"
            if context.entity["type"] == "Shot" and shot_type == "showroom" and context.step["name"] == "SPR":
                return "showroom_step_sprite"
            if context.entity["type"] == "Shot" and shot_type == "showroom" and context.step["name"] == "DFT":
                return "showroom_step_render"
            if context.entity["type"] == "Shot" and shot_type == "showroom" and context.step["name"] == "RND":
                return "showroom_step_render"
            if context.entity["type"] == "Asset":
                return "asset_step"
            if context.entity["type"] == "CustomEntity01":
                return "material_step"
            if context.entity["type"] == "CustomEntity02":
                return "scene_step"
        return None