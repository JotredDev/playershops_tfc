package net.jotred.playershops_tfc.common.blockentities;

import com.talons.playershops.block.entity.custom.PlayerShopBlockEntity;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;

public class PlayerShopAFCBlockEntity extends PlayerShopBlockEntity {
	
	public PlayerShopAFCBlockEntity(BlockPos position, BlockState state) {
		super(PlayershopsAFCBlockEntities.PLAYER_SHOPS_AFC.get(), position, state);
	}
}