package net.jotred.playershops_tfc.common.blockentities;

import net.dries007.tfc.util.Helpers;
import net.dries007.tfc.util.registry.RegistrationHelpers;

import net.jotred.playershops_tfc.common.blocks.PlayershopsAFCBlocks;

import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

import java.util.function.Supplier;
import java.util.stream.Stream;

public class PlayershopsAFCBlockEntities {
	
	public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITIES_AFC =
		DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, "playershops_tfc");
	
	public static final RegistryObject<BlockEntityType<PlayerShopAFCBlockEntity>> PLAYER_SHOPS_AFC =
		register("player_shops_afc",
			PlayerShopAFCBlockEntity::new,
			Stream.of(PlayershopsAFCBlocks.AFC_WOOD_PLAYER_SHOP_BLOCKS.values())
				.<Supplier<? extends Block>>flatMap(Helpers::flatten));
	
	
	private static <T extends BlockEntity> RegistryObject<BlockEntityType<T>> register(String name, BlockEntityType.BlockEntitySupplier<T> factory, Stream<? extends Supplier<? extends Block>> blocks)
	{
		return RegistrationHelpers.register(BLOCK_ENTITIES_AFC, name, factory, blocks);
	}
}
