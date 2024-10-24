package net.jotred.playershops_tfc.common.blockentities;

import net.jotred.playershops_tfc.common.blocks.PlayershopsTFCBlocks;

import java.util.function.Supplier;
import java.util.stream.Stream;

import net.minecraft.world.level.block.*;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

import net.dries007.tfc.util.Helpers;
import net.dries007.tfc.util.registry.RegistrationHelpers;

public class PlayershopsTFCBlockEntities {
	
	public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITIES =
		DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, "playershops_tfc");
	
	public static final RegistryObject<BlockEntityType<PlayerShopTFCBlockEntity>> PLAYER_SHOPS =
		register("player_shops",
			PlayerShopTFCBlockEntity::new,
			Stream.of(PlayershopsTFCBlocks.TFC_WOOD_PLAYER_SHOP_BLOCKS.values())
				.<Supplier<? extends Block>>flatMap(Helpers::flatten));
	
	
	private static <T extends BlockEntity> RegistryObject<BlockEntityType<T>> register(String name, BlockEntityType.BlockEntitySupplier<T> factory, Stream<? extends Supplier<? extends Block>> blocks)
	{
		return RegistrationHelpers.register(BLOCK_ENTITIES, name, factory, blocks);
	}
}
