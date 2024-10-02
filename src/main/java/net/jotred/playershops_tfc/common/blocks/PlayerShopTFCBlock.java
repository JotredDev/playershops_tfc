package net.jotred.playershops_tfc.common.blocks;

import com.talons.playershops.block.custom.PlayerShopBlock;
import net.jotred.playershops_tfc.common.blockentities.PlayerShopTFCBlockEntity;
import net.minecraft.core.BlockPos;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.entity.BlockEntityTicker;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.level.block.state.BlockState;

import javax.annotation.Nullable;

public class PlayerShopTFCBlock extends PlayerShopBlock {
	
	public PlayerShopTFCBlock (Properties properties) {
		super (properties);
	}
	
	@Nullable
	@Override
	public BlockEntity newBlockEntity (BlockPos position, BlockState state) {
		return new PlayerShopTFCBlockEntity(position, state);
	}
	
	@Nullable
	@Override
	public <T extends  BlockEntity> BlockEntityTicker<T> getTicker (Level level, BlockState state, BlockEntityType<T> type) {
		return PlayerShopTFCBlockEntity::tick;
	}
}
