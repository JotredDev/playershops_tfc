package net.jotred.playershops_tfc.common.blockentities;

import com.talons.playershops.block.entity.custom.PlayerShopBlockEntity;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;

public class PlayerShopTFCBlockEntity extends PlayerShopBlockEntity {
	
	public PlayerShopTFCBlockEntity (BlockPos position, BlockState state) {
		super(PlayershopsTFCBlockEntities.PLAYER_SHOPS.get(), position, state);
	}
}